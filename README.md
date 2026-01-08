<img width="1402" height="932" alt="image" src="https://github.com/user-attachments/assets/93f320e6-cbdb-425c-a9e4-4eac2cfd801d" />
# FLIR ONE 照片轉換工具 (FLIR ONE Image Conversion Tool)

**製作人：台中市立惠文高中 地球科學 吳秉勳教師**
**Developed by: Bing-Syun Wu, Earth Science Teacher, Taichung Municipal Hui-Wen High School**

---

## 🇹🇼 中文使用說明

### 1. 下載 ExifTool
* 1-1. 前往 [ExifTool 官網](https://exiftool.org/index.html) 下載 Windows 執行檔 (Windows Executable)。
* 1-2. 解壓縮後，會得到一個名為 `exiftool(-k).exe` 的檔案。
* 1-3. **重要：** 請將 `exiftool(-k).exe` 手動重新命名為 **`exiftool.exe`**。

### 2. 放置檔案
* 2-1. 請確保本程式 (`flir_tool.exe` 或 `flir_tool.py`) 與 `exiftool.exe` 放在 **同一個資料夾** 中。
* 2-2. `flir_tool.exe` 可直接在 Windows 系統中執行，或使用 Python 執行 `flir_tool.py`。

### 3. 功能操作
* **3-1. 開啟照片**：選取單張 FLIR JPG 照片，右側會自動顯示提取出的可見光畫面。
* **3-2. 存檔可見光**：將目前顯示的可見光照片另存新檔。
* **3-3. 批次提取**：一次選取多張照片，程式會自動完成所有照片的提取與存檔。

> **備註：** 程式會自動偵測執行檔所在路徑來呼叫 `exiftool`；若執行時跳出「找不到工具」的錯誤，請檢查 `exiftool.exe` 是否正確命名並置於程式旁。

## 📸 應用範例 (Applications)
可以參考以下網頁，查看使用 FLIR ONE 拍攝大屯火山區的實際案例與照片：
* **大屯火山群觀測範例**：https://sites.google.com/view/earthscienceworld/geology/volcanology/tatun

---

## 🇺🇸 English Instructions

### 1. Installation & Setup
* 1-1. Go to the [ExifTool official website](https://exiftool.org/index.html) and download the **Windows Executable**.
* 1-2. After extracting the downloaded ZIP file, you will find a file named `exiftool(-k).exe`.
* 1-3. **Important:** Manually rename `exiftool(-k).exe` to **`exiftool.exe`**.

### 2. File Placement
* 2-1. Ensure that this program (`flir_tool.exe` or `flir_tool.py`) and **`exiftool.exe`** are located in the **same folder**.
* 2-2. You can run `flir_tool.exe` directly on Windows, or execute `flir_tool.py` using Python.

### 3. Features
* **3-1. Open Photo**: Select a single FLIR JPG photo. The extracted visible light image will automatically appear on the right pane.
* **3-2. Save Visible Photo**: Save the currently displayed visible light image as a new file.
* **3-3. Batch Extraction**: Select multiple photos at once; the program will automatically extract and save the visible light layers for all selected files.

> **Notes:** The program automatically detects its own directory to call `exiftool`. If a "Tool not found" error occurs, please double-check that `exiftool.exe` is named correctly and placed in the same folder as the program.

---

**版權所有 © 台中市立惠文高中 地球科學 吳秉勳教師** **Copyright © Bing-Syun Wu, Earth Science Teacher, Taichung Municipal Hui-Wen High School**



