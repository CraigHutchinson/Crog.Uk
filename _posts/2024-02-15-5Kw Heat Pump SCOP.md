---
layout: post
title:  "5Kw Heat Pump SCOP (EN 14511)"
date:   2024-02-15 11:14:02 +0000
categories: Heat Pump
---

I've been collating all the heat-pump SCOP (Seasonal Coefficient Of Performance) figures for models I am aware of.

TODO: EN-14825 replaced by EN-14511 ??
* EBac EN-14825 to now EN-14511 reduced from 5.11 to 4.91 @35C, 4.73 to 4.63 @ 45C, 4.12 to 3.96 @ 55C [old-datasheet](https://ebac-serverless.files.svdcdn.com/production/default/EBA%E2%80%A2230341_AIR-SOURCE-HEAT-PUMP-E-BROCHURE_HOT-WATER-CYLINDER.pdf?dm=1695277753)

Criteria:
- Target property 4-5Kw
- EN 14511 Average Climate
- Ordered by SCOP where higher is better. Where order is ambiguous the SCOP at 45C is used.

** = models may underperform due to cycling as these models are 8KW+

() = SCOP at 45C calculated as MEAN(35,55) when not made available in datasheet.
 This produces conservative underestimate of SCOP when unavailable.

 !! SCOP standard OLD or NOT-DEFINED - results may be of question

| Make/Model              | SCOP-Standard | SCOP@35C | SCOP@45C | SCOP@55C | Gas  | Comment              | Specification Date | Site/Datasheet |
| ----------------------: | ------------- | :------- | :------- | :------- | ---: | -------              | ------------------ | --- |
| Ovum AC208P **          | !! EN-14825   | 5.78     |          | 4.15     | R290 |                     | 2024-01            | [site](https://www.ovum.at/en/produkte/luft-die-koenigsklasse/) [datasheet](https://www.ovum.at/wp-content/uploads/2023/10/ACP_Datenblatt_alle_Web_230928.pdf) |
| Lambda 8Kw **           | EN-14511      | 5.66     |          | 4.48     | R290 |                      | 2024-01            | [site](https://lambda-wp.at/luft-waermepumpen/) [datasheet](https://assets-global.website-files.com/643186efcbc3b72e2a4f6db8/65acf5477b9a14bfd7615549_Scheda%20Tecnica.pdf)|
| EBac 5Kw                | EN-14511      | 4.91     |  4.63    | 3.96     | R32  |                      | 2024-02            | [datasheet](https://files.ebac.com/production/default/EBA%E2%80%A2240014_HEATPUMP-DATASHEET_QR_LR_2024-02-10-072606_tqkz.pdf?dm=1707549967) |
| LG Therma V 9Kw **      | !! N/A        | 5.23     | (4.49)   | 3.75     | R290 |                      | 2024-01            | [datasheet](https://www.lg.com/global/business/download/airsolution/THERMA%20V%20(AWHP)%20R290%20Monobloc%20Hydro%20Unit%208P%20%20leaflet_web_Holo_O_1117_low[20240130_154102737].pdf) |
| Ideal 5Kw               | !! EN-14825   | 5.07     | (4.36)   | 3.65     | R32  |                      | {todo}             | [site](https://idealtouch.co.uk.idealboilers.com/products/logic-air-heat-pump-3) |
| Nibe 6kw **             | !! EN-14825   | 5.08     |          | 3.58     | R32  |                      | {todo}             | [datasheet](https://assetstore.nibe.se/hcms/v2.3/entity/document/874828/storage/ODc0ODI4LzAvbWFzdGVy) |
| Bosch 5800i 5Kw         | {todo}        | 4.65     |          | 3.50     | R290 | {todo} Source of figures !? | {todo}       | [site](https://www.worcester-bosch.co.uk/products/heat-pumps/directory/compress-5800i-aw)  |
| Samsung Gen7 5Kw        | {todo}        | 4.84     |  4.14    | 3.42     | R290 |                      | {todo}             | [datasheet](https://midsummerwholesale.co.uk/pdfs/samsung-gen-7-r290-datasheet.pdf) |
| Viessmann 151.A06       | {todo}        | 4.58     | (4.10)   | 3.61     | R290 | {todo} 3.61 is-at 55? | {todo}            | [datasheet](https://viessmanndirect.co.uk/files//7a81a248-e65a-4fcf-8735-e4a33fa33fe4/Energy%20Consumption%20Datasheet.pdf) |
| Mitsubishi Ecodan       | {todo}        | 4.62     | (4.08)   | 3.53     | R290 |                      | {todo}             | [site](https://library.mitsubishielectric.co.uk/pdf/book/EcodanR290Outdoor1#page-1) |
| Baxi  5Kw               | {todo}        | 4.77     |  4.06    | 3.39     | R32  |                      | {todo}             | [site](https://www.baxi.co.uk/new-build/products/air-source-heat-pumps/baxi-assure-hp50-ashp) |
| Daikin Altherma 4Kw     | {todo}        | 4.48     | (3.87)   | 3.26     | R32  |                      | {todo}             | [site](https://www.daikin.co.uk/en_gb/products/product.table.html/EDLA04-08E3V3.html) |
| Vaillant aroTherm+ 5Kw  | EN-14511      | 4.48     |  3.77    | 3.06     | R290 |                      | {todo}             | [datasheet](https://professional.vaillant.co.uk/downloads/aproducts/renewables-1/arotherm-plus/arotherm-plus-spec-sheet-1892564.pdf) |

