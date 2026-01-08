# 版權宣告：台中市立惠文高中地球科學吳秉勳教師製作

import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import subprocess
import io
import os
import sys

class FlirPortableFix:
    def __init__(self, root):
        self.root = root
        # 更新視窗標題包含版權資訊
        self.root.title("FLIR ONE 照片轉換工具 - 台中市立惠文高中地球科學吳秉勳教師製作")
        self.root.geometry("1400x900")
        self.root.configure(bg="#121212")

        # 自動偵測 exiftool.exe 路徑 (相容開發環境與打包後的 exe)
        if getattr(sys, 'frozen', False):
            base_dir = os.path.dirname(sys.executable)
        else:
            base_dir = os.path.dirname(os.path.abspath(__file__))
            
        self.exiftool_path = os.path.join(base_dir, "exiftool.exe")
        
        self.original_path = ""
        self.thermal_pil = None
        self.visible_pil = None
        self.tk_t = None
        self.tk_v = None
        self.btn_font = ("微軟正黑體", 28, "bold")

        self.setup_ui()

    def setup_ui(self):
        self.top_bar = tk.Frame(self.root, bg="#333")
        self.top_bar.pack(side=tk.TOP, fill=tk.X)
        
        tk.Button(self.top_bar, text="📁 開啟照片", command=self.load_flir, 
                  bg="#007acc", fg="white", padx=20, font=self.btn_font).pack(side=tk.LEFT, padx=10, pady=15)
        
        tk.Button(self.top_bar, text="💾 存檔可見光", command=self.save_visible_only, 
                  bg="#28a745", fg="white", padx=20, font=self.btn_font).pack(side=tk.LEFT, padx=10)

        tk.Button(self.top_bar, text="🚀 批次提取", command=self.batch_process, 
                  bg="#e67e22", fg="white", padx=20, font=self.btn_font).pack(side=tk.LEFT, padx=(80, 10))

        self.main_area = tk.Frame(self.root, bg="#121212")
        self.main_area.pack(expand=True, fill=tk.BOTH)

        self.t_label = tk.Label(self.main_area, bg="black")
        self.t_label.place(relx=0, rely=0, relwidth=0.5, relheight=1.0)
        self.v_label = tk.Label(self.main_area, bg="black")
        self.v_label.place(relx=0.5, rely=0, relwidth=0.5, relheight=1.0)

        self.root.bind("<Configure>", lambda e: self.refresh_images() if self.thermal_pil else None)

    def load_flir(self):
        if not os.path.exists(self.exiftool_path):
            messagebox.showerror("錯誤", f"找不到工具！\n請確認 exiftool.exe 是否放在：\n{self.exiftool_path}")
            return

        path = filedialog.askopenfilename(filetypes=[("FLIR JPG", "*.jpg")])
        if not path: return
        self.original_path = path
        try:
            self.thermal_pil = Image.open(path).convert("RGB")
            res = None
            # 支援多種 FLIR 標籤以提升相容性
            for tag in ["-EmbeddedImage", "-VisibleImage", "-FLIR:VisibleImage", "-PreviewImage"]:
                cmd = [self.exiftool_path, tag, "-b", path]
                # 設定隱藏執行時的黑色 CMD 視窗
                si = subprocess.STARTUPINFO()
                si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
                res = subprocess.run(cmd, stdout=subprocess.PIPE, startupinfo=si).stdout
                if res and len(res) > 1000: break
            
            self.visible_pil = Image.open(io.BytesIO(res)).convert("RGB") if res else None
            self.refresh_images()
        except Exception as e:
            messagebox.showerror("錯誤", f"讀取失敗: {e}")

    def refresh_images(self):
        self.root.update_idletasks()
        total_w, total_h = self.main_area.winfo_width(), self.main_area.winfo_height()
        max_w, max_h = (total_w // 2) - 20, total_h - 40
        if max_w < 50: return

        for img, label, attr in [(self.thermal_pil, self.t_label, 'tk_t'), (self.visible_pil, self.v_label, 'tk_v')]:
            if img:
                ratio = min(max_w / img.width, max_h / img.height)
                new_size = (int(img.width * ratio), int(img.height * ratio))
                tk_img = ImageTk.PhotoImage(img.resize(new_size, Image.Resampling.LANCZOS))
                setattr(self, attr, tk_img)
                label.config(image=tk_img, text="")
            elif label == self.v_label:
                label.config(image="", text="此照片無可見光層", fg="white", font=("微軟正黑體", 20))

    def save_visible_only(self):
        if not self.visible_pil: return
        base, ext = os.path.splitext(self.original_path)
        save_path = f"{base}_visible{ext}"
        self.visible_pil.save(save_path, "JPEG", quality=95)
        messagebox.showinfo("成功", f"已存檔：{os.path.basename(save_path)}")

    def batch_process(self):
        paths = filedialog.askopenfilenames(filetypes=[("FLIR JPG", "*.jpg")])
        if not paths: return
        success = 0
        si = subprocess.STARTUPINFO()
        si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        for p in paths:
            res = None
            for tag in ["-EmbeddedImage", "-VisibleImage", "-FLIR:VisibleImage", "-PreviewImage"]:
                res = subprocess.run([self.exiftool_path, tag, "-b", p], stdout=subprocess.PIPE, startupinfo=si).stdout
                if res and len(res) > 1000: break
            if res:
                with open(f"{os.path.splitext(p)[0]}_visible.jpg", "wb") as f: f.write(res)
                success += 1
        messagebox.showinfo("完成", f"已批次處理 {success} 張照片。")

if __name__ == "__main__":
    root = tk.Tk()
    app = FlirPortableFix(root)
    root.mainloop()