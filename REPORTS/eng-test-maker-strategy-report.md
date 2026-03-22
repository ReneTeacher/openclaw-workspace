# Eng-Test-Maker 商業策略顧問報告

**顧問身份：** McKinsey 風格商業顧問  
**調研日期：** 2026年3月21日  
**機密等級：** 僅供 Rene (Teacher) 參考

---

## 執行摘要

Eng-Test-Maker 係一個已有完整 AI 自動化流程嘅英文科考試系統，核心功能（聽寫自動批改 + 影相上傳 OCR + Email 成績報告）已超出多數競爭對手。但係距離商業化仲有 5 個關鍵缺口：訂閱系統、品牌包裝、用戶入門門檻、定價策略、以及 API 成本控制。

---

## 第一部分：市場研究

### 1.1 競爭對手全景圖

| 競爭對手 | 類型 | 定價 | 強項 | 弱項 |
|---------|------|------|------|------|
| **MagicSchool AI** | 全科老師工具平台 | 免費 / $12.99/月（個人）/ 學校版自訂 | 80+ 工具、Chrome 插件、學校管理後台 | 非專科、冇本地 DSE 格式、AI 生成試卷非即時批改 |
| **Gradescope** | 全科在線評分 | 學校版 $699/老師/年 | 已流行、品牌成熟 | 主要係客觀題、冇 AI 即時批改、冇 Email 自動報告 |
| **GradeLab** | AI 作文批改平台 | 未公開（要聯絡 sales） | AI 作文批改、1000+ 機構信任 | 主力英文作文、非亞洲市場、學校 B2B 為主 |
| **ExamAI** | AI 試卷生成+評分 | 未公開 | AI 生成試卷+評分一體 | 產品新、未見香港/澳門市場滲透 |
| **CoGrader** | AI 作文批改 | 學校版有 PO 付款 | 老師直接上傳文件 | 非即時、主力作文、香港陌生 |
| **科大訊飛** | 全校 AI 教育系統 | 學校年度授權（估計 HK$50,000-500,000/年） | 全校系統、國家隊背景、關係分銷網 | 學校決策層、無法個人老師使用、DSE/英文非核心 |

### 1.2 市場定位地圖

```
                    高價格
                        │
                        │
    DSE 英文專科         │    [科大訊飛]
    [Eng-Test-Maker]    │
    [ExamAI]            │
                        │
    多科目平台           │    [MagicSchool]
    [Gradescope]        │
                        │
                        └──────────────────────────── 低價格
                         學校 B2B              個人老師 SaaS
```

**你嘅位置：DSE 英文專科 × 個人老師 SaaS**  
呢個 quadrant 目前競爭最少，但係市場最大需求喺哪一邊（學校 B2B 定個人老師）需要驗證。

### 1.3 市場規模估算（香港/澳門）

- 香港中小學英文科老師：約 8,000-10,000 人
- 澳門中小學英文科老師：約 800-1,000 人
- 願意付費比例（參考 MagicSchool 模式）：約 5-15%
- 可觸及市場（TAM with pricing $10-15/月）：HK$40,000-165,000/月

### 1.4 行業趨勢

1. **AI 評分工具爆發**：2025-2026 年大量工具湧現，老師逐漸接受 AI 輔助批改
2. **學校 B2B 決策周期長**：6-18 個月，需要關係網絡
3. **個人老師 SaaS 增長快**：用信用卡月付，門檻低
4. **家長付費意願存在**：家長願意為子女教育付費，但需要 school endorsement
5. **DSE 格式壁壘高**：本地化係最大差異化機會

---

## 第二部分：現有系統功能評估

### 2.1 功能完整性評分

| 功能模組 | 現狀 | 評分 | 備註 |
|---------|------|------|------|
| 老師建立試卷 | ✅ | 8/10 | Quick Build 工具完善 |
| 聽寫自動朗讀 | ✅ | 8/10 | pyttsx3，本地運行 |
| 學生登入系統 | ✅ | 7/10 | 有，但冇 OAuth |
| 影相上傳 OCR | ✅ | 7/10 | Poe API，穩定 |
| AI 答案批改 | ✅ | 7/10 | MiniMax + Poe，邏輯正確 |
| Email 成績報告 | ✅ | 6/10 | 有，但 SMTP 設定複雜 |
| 學校管理後台 | ❌ | 2/10 | 欠缺 |
| 定價/訂閱系統 | ❌ | 0/10 | 完全欠缺 |
| 用家指南/介紹頁 | ❌ | 0/10 | 完全欠缺 |
| API Key 隱藏 | ❌ | 0/10 | 用緊環境變數，但係部署設定有風險 |

### 2.2 API 使用現狀分析

你目前使用三個主要 API：

#### A. MiniMax API（abab6.5s-chat）
- **用途**：AI 句子分割、語意比對、詞彙評分
- **問題**：
  - 暴露喺 client-side code（`import.meta.env.VITE_*`）
  - API key 存喺 deployment environment（正確做法）
  - 但 `MINIMAX_API_KEY` 同 `POE_API_KEY` 都有被引用
- **成本估算**：
  - abab6.5s-chat：輸出 tokens 約 $0.015/千tokens（估計）
  - 每個 submission 估計 500-2000 output tokens
  - 每100個學生submission：約 $1-4（MiniMax部分）

#### B. Poe API（Claude/GPT）
- **用途**：OCR 圖片理解 + 句子 matching（`aiMatchStudentToSentences`）
- **問題**：
  - 走 Poe proxy 係聰明嘅做法（避免直接暴露 API key）
  - 但係 POE_API_KEY 同樣在 server-side 環境變數
- **成本估算**：
  - Poe 按用量收費，Claude/GPT 3.1 Flash 便宜
  - 每個 OCR + matching 估計 $0.002-0.01/submission
  - 每100個學生submission：約 $0.2-1

#### C. SMTP Email（Nodemailer）
- **用途**：成績報告 Email 發送到學生
- **問題**：
  - SMTP 設定複雜
  - 需要老師自己設定 SMTP（Eng-Test-Maker 內）
  - Gmail SMTP 容易被block，需要第三方 Transactional Email Service

### 2.3 API 成本模型

**場景：100個學生/月/老師**

| API 呼叫 | 次數 | 估計成本 |
|---------|------|---------|
| MiniMax AI 評分 | 100次 | $1-4 |
| Poe OCR + Matching | 100次 | $0.2-1 |
| Email（SES/SendGrid） | 100封 | $0.1 |
| **合計** | | **$1.3-5.1/老師/月** |

**如果你收 $15/老師/月：**
- 利潤空間：$10-13/老師/月（未計 server 費用）
- Server 費用（Render 免費 tier + Supabase）：約 $0-20/月

**關鍵洞察：API 成本非常低，利潤空間充足。**

---

## 第三部分：最關鍵的 5 個缺口

### Gap 1：❌ 沒有訂閱收費系統（最高優先級）

**問題**：完全冇收費機制，全部功能免費使用。

**解決方案**：

方案 A：**Stripe 訂閱（推薦）**
- Stripe Billing 支援月/年訂閱
- 接入簡單，有成熟的 SaaS 模板
- 支持信用卡、HK FPS

方案 B：**LemonSqueezy（更簡單）**
- 專為 SaaS 設計，唔需要自己開 Stripe 帳戶
- 自帶全球合規（歐盟 VAT 等）
- 但係香港支援稍差

方案 C：**Paddle**
- B2B SaaS 付款處理，支援Purchase Order
- 適合學校 B2B

**建議**：Stripe + LemonSqueezy 並行

### Gap 2：❌ SMTP 設定複雜（高優先級）

**問題**：老師需要自己設定 SMTP 才能讓 Email 功能正常運作，完全係 friction。

**解決方案**：

**方案 A：Resend（推薦）**
- 免費100封/日，超出 $20/1000封
- API 簡單，一行代碼接入
- 不容易被 Gmail block

**方案 B：SendGrid**
- 免費100封/日，超出 $15/1000封
- 成熟穩定

**方案 C：AWS SES**
- 最便宜 $0.1/1000封
- 但設定複雜，需要 AWS 帳戶

**你嘅 Eng-Test-Maker 只需更換 nodemailer transport，10分鐘完成。**

### Gap 3：❌ 用家需要設定 API Key（高優先級）

**問題**：你自己用緊 API key，但係其他老師用你嘅系統唔需要自己set key——呢個係你嘅優勢，但係需要確認你嘅 API key唔會被濫用。

**評估**：
- 目前你嘅架構係所有 AI 評分喺 server-side 進行 ✅
- 老師/學生完全接觸唔到 API key ✅
- 用家體驗：只需要上網址、登入、用 ✅

**呢個已經係正確嘅方向！** 唔需要改。

### Gap 4：❌ 沒有 Landing Page / 介紹頁（高優先級）

**問題**：冇任何 marketing page，其他老師打開個網址只係登入頁，完全唔知呢個係乜。

**解決方案**：
- 建立一個簡單嘅 landing page（單頁 HTML/CSS）
- 包含：產品截圖、功能介紹、定價、聯絡
- 可以 deploy 上 Vercel/Cloudflare Pages（免費）

### Gap 5：❌ 沒有品牌和信任建立（中優先級）

**問題**：冇品牌名、冇介紹、冇 social proof。

**解決方案**：
- 命名 Eng-Test-Maker → 建立品牌
- 建立 1 個 teacher case study（你自己嘅使用經驗）
- 如果可以：加一句老師 testimonial

---

## 第四部分：如何做到「用家不需要設置任何 API」

### 核心原則：用家只接觸 UI，所有 API 調用喺 server-side 進行

你現有架構已經係咁 ✅

**你嘅用家旅程應該係：**

```
老師 → 註冊（Google Login 一鍵）→ 選擇計劃（Stripe 付款）→ 建立試卷 → 分享連結俾學生
                                        ↓
學生 → 連結 → 登入 → 拍照上傳答卷 → 自動批改 → Email 收到成績報告
```

**所有 AI 調用都喺你嘅 server（Render）入面發生，用家完全接觸唔到 API key。**

### 用家需要設定的 0 樣嘢（目標）：

| 需要設定的 | 現狀 | 目標 |
|-----------|------|------|
| API Key | ❌（server-side） | ❌（保持） |
| SMTP | ❌（server-side） | ❌（保持） |
| 數據庫 | ❌（Supabase） | ❌（保持） |
| 信用卡設定 | ❌ | ✅ Stripe |
| 學校帳戶 | ❌ | ✅ Stripe/學校版 |

---

## 第五部分：訂閱系統實作指南

### 5.1 Stripe 訂閱模式推薦

**模式一：按老師月費（適合個人老師）**
| 計劃 | 價格 | 包含 |
|------|------|------|
| Free | $0 | 3個試卷/月、20個學生 |
| Basic | $10/月 | 20個試卷/月、200個學生 |
| Pro | $20/月 | 無限試卷、無限學生 |

**模式二：按用量收費（跟 student submissions）**
- $0.05-0.10/每個學生 submission
- 優點：用幾多付幾多
- 缺點：收入唔穩定

**模式三：學校授權（B2B）**
- $50-200/月/學校
- 包含所有老師
- 需要 admin dashboard

**推薦**：先做模式一（個人老師），再做模式三（學校 B2B）

### 5.2 Stripe 接入步驟（極簡版）

1. 申請 Stripe 帳戶
2. 開通 Stripe Billing
3. 建立 3 個產品（Free/Basic/Pro）
4. 喺 server 加入 Stripe webhook
5. 喺前端加入 checkout button
6. 設定 usage limit logic

**預計工時**：4-8 小時（如果你熟 Node.js）

### 5.3 LemonSqueezy（更簡單替代）

如果你想要更快嘅方案：
1. 申請 LemonSqueezy
2. 建立產品
3. 複製 checkout embed code
4. 放到 landing page

**預計工時**：1-2 小時（無需 server code 改動）

---

## 第六部分：API 成本控制策略

### 6.1 成本分析（你目前的 API 使用）

**你目前的 API 成本（假設 1 個老師，100 個學生/月）**

| API | 用量 | 成本 |
|-----|------|------|
| MiniMax（評分） | 100次 × 1000 tokens | $1-3 |
| Poe（OCR + matching） | 100次 × 5000 tokens | $0.5-2 |
| Email | 100封 | $0.1 |
| Supabase | - | $0（免費 tier） |
| Render | - | $0（免費 tier） |
| **合計** | | **$1.6-5.1/月** |

**如果你收 $15/月：**
- 毛利：$10-13/月/老師 ✅

### 6.2 成本優化策略

**1. 減少不必要的 AI 調用**
- 如果學生的答案是明顯空白，可以跳過 AI 評分
- caching 相同試卷的正確答案比對結果

**2. 使用更便宜的模型**
- MiniMax abab6.5s-chat 已經係便宜選擇 ✅
- 可以考慮 MiniMax 更大模型但有更少 token

**3. Batch submission 評分**
- 老師可以設定「每日統一評分」而不是即時評分
- 可以降低 API 調用頻率

**4. 用量上限**
- Free plan：20 個 submission/月
- Basic plan：200 個 submission/月
- 超過自動升級提示

### 6.3 你目前的 API Key 管理

**現狀評估**：
- `MINIMAX_API_KEY` → server-side env ✅
- `POE_API_KEY` → server-side env ✅
- `DATABASE_URL` → server-side env ✅
- `SMTP_*` → server-side env ✅

**建議**：
- 將所有 API keys 移到 Render 的 Environment Variables（而非 .env 檔案）
- 確認 MINIMAX_API_KEY 同 POE_API_KEY 唔會 log 出來
- 考慮用 Vercel 替換 Render（更快、更穩定）

---

## 第七部分：產品改善藍圖

### Phase 1（1-2個月）：立即可商業化 ✅
- [ ] 加入 Stripe 訂閱系統
- [ ] 切換到 Resend Email
- [ ] 建立 Landing Page
- [ ] 設定 3 個訂閱計劃（Free/Basic/Pro）

### Phase 2（3-4個月）：增加功能護城河
- [ ] 老師可以自定義題目格式模板
- [ ] 學生家長 Email 通知
- [ ] 學生歷史分數圖表
- [ ] 老師試卷資料庫（bank）

### Phase 3（6個月+）：學校 B2B 擴張
- [ ] 學校 admin dashboard
- [ ] SSO（Google/Microsoft 登入）
- [ ] 學校內老師管理
- [ ] Purchase Order 付款

---

## 第八部分：竞争壁垒分析

### 點解你比科大訊飛更有競爭力？

| 維度 | 科大訊飛 | Eng-Test-Maker |
|------|---------|----------------|
| 入門門檻 | 學校 IT 介入 | 老師自己 5 分鐘上手 ✅ |
| DSE 英文格式 | 內地試卷格式 | 完全支持 ✅ |
| 個人化 | 全校統一 | 老師個人化 ✅ |
| 價錢 | HK$50,000+/年（估計） | $10-20/月 ✅ |
| AI 批改 | 有但非核心 | 核心功能 ✅ |
| Email 即時報告 | 可能無 | 有 ✅ |

### 你真正嘅競爭壁壘

1. **本地化**：DSE 英文格式係大公司唔會特別為澳門/香港優化嘅細節
2. **速度**：你一個人可以每週更新，大公司需要幾個月決策
3. **用家體驗**：老師自己 set up 唔需要 IT，大公司需要學校部署
4. **價錢**：月費模式比年授權靈活，老師風險低

---

## 第九部分：關鍵問題清單（你需要答）

在實作之前，你需要明確以下問題：

1. **你想sell俾邊個？**
   - 個人老師（自己搵客）？
   - 學校（靠朋友關係入圍）？

2. **你肯幾多時間落去？**
   - Side project（業餘）？
   - 全職 startup？

3. **你嘅 initial user 係邊個？**
   - 你自己？
   - 你嘅老師 friend？

4. **你想要幾多收入先算成功？**
   - 第一年：HK$100,000？
   - 第一年：HK$500,000？

5. **你肯幾時開始收錢？**
   - 6 個月內？
   - 等有100個 user 先？

---

## 第十部分：行動建議

### 立即（呢個星期）

1. ✅ 將 Eng-Test-Maker 正式命名，建立品牌
2. ✅ 建立 Stripe 帳戶（未需要接入，先申請）
3. ✅ 申請 Resend 帳戶（替換 SMTP）
4. ✅ 建立簡單 landing page（在 Vercel）

### 30 天內

1. 接入 Stripe Billing（3個訂閱計劃）
2. 切換 email 到 Resend
3. 聯絡 3-5 個老師 friend 做 user interview
4. 設定 landing page 配合推廣

### 90 天內

1. 正式 launch 收費版本
2. 搵 5-10 個付費用戶
3. 根據用戶 feedback 迭代

---

## 附錄：競爭對手 Landing Page 參考

- MagicSchool：https://www.magicschool.ai/pricing ✅ 定價清晰
- Gradescope：https://www.gradescope.com/ ✅ 學校 B2B 參考
- CoGrader：https://cograder.com/ ✅ 作文 AI 批改

---

**報告完成**
*如有需要，我可幫你實作任何一個部分（Stripe 接入、Landing Page、Email 系統切換等）*
