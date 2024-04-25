---
layout: post
title:  "Comparison of 5Kw Heat Pumps"
date:   2024-02-15 11:14:02 +0000
modified_date: 2024-04-25 08:18:00 +0000
categories: HeatPump
datatable: true
pinned: false
---

This is a comparison table of all 2024-2025 heat-pump datasheet figures for make+models I am aware of.

Criteria:
- Target property 4-5Kw
- EN 14511/14825 (?) Average Climate and Low temperature = 35C and Medium = 55C
- Ordered by SCOP where higher is better. Where order is ambiguous the SCOP at 45C is used, and then 35C i.e. We prefer mild weather performance which gives greater yearly SCOP.


<div class="datatable-begin"></div>

| Make/Model              | Standard      | SCOP@35C | SCOP@45C | SCOP@55C | Gas  | Comment              | Specification Date | Site/Datasheet |
| [<sup>1</sup>](#k_make) | [<sup>2</sup>](#k_std)|  | [<sup>3</sup>](#k_45) | |  |                      |                    |                |
| ----------------------: | ------------- | :------- | :------- | :------- | ---: | -------------------- | ------------------ | -------------- |
| `Lambda 8Kw`            | EN-14511      | 5.66     | `5.07`   | 4.48     | R290 |                      | 2024-01            | [site](https://lambda-wp.at/luft-waermepumpen/) [datasheet](https://assets-global.website-files.com/643186efcbc3b72e2a4f6db8/65acf5477b9a14bfd7615549_Scheda%20Tecnica.pdf)|
| `Ovum AC208P`           | EN-14825      | 5.53     | `4.89`   | 4.00     | R290 |                      | 2024-02            | [site](https://www.ovum.at/en/produkte/luft-die-koenigsklasse/) [datasheet](https://www.ovum.at/wp-content/uploads/2024/02/ACP_Datenblatt_alle_web_240206.pdf) |
| `LG Therma V 9Kw`       | `NOT-DEFINED` | 5.23     | `4.49`   | 3.75     | R290 |                      | 2024-01            | [datasheet](https://www.lg.com/global/business/download/airsolution/THERMA%20V%20(AWHP)%20R290%20Monobloc%20Hydro%20Unit%208P%20%20leaflet_web_Holo_O_1117_low[20240130_154102737].pdf) |
| EBac H1A05WG-GB 5Kw     | EN-14511      | 4.91     |  4.38    | 3.96     | R32  |                      | 2024-02            | [site](https://www.ebac.com/air-source-heat-pump) [datasheet](https://files.ebac.com/production/default/EBA%E2%80%A2240014_HEATPUMP-DATASHEET_QR_LR_2024-02-10-072606_tqkz.pdf?dm=1707549967) [brochure](https://files.ebac.com/production/default/EBA%E2%80%A2240014_AIR-SOURCE-HEAT-PUMP-E-BROCHURE_HOT-WATER-CYLINDER_LR.pdf?dm=1707549642&_gl=1*13a0crf*_ga*ODYzOTEyOTE1LjE3MDIzODE4NDc.*_ga_6WDFCXQC67*MTcxMDg0OTQxMC4yNC4wLjE3MTA4NDk0MTIuNTguMC4w) |
| Ideal 5Kw               | EN-14825      | 5.07     | `4.36`   | 3.65     | R32  |                      | 2023-06            | [site](https://idealtouch.co.uk.idealboilers.com/products/logic-air-heat-pump-3) |
| Nibe 6kw                | EN-14825      | 5.08     | `4.33`   | 3.58     | R32  |                      | {todo}             | [datasheet](https://assetstore.nibe.se/hcms/v2.3/entity/document/874828/storage/ODc0ODI4LzAvbWFzdGVy) |
| Bosch 5800i 5Kw         | {todo}        | 4.65     | `4.08`   | 3.50     | R290 | {todo} Data source!? | {todo}             | [site](https://www.worcester-bosch.co.uk/products/heat-pumps/directory/compress-5800i-aw)  |
| Samsung Gen7 5Kw        | {todo}        | 4.84     |  4.14    | 3.42     | R290 |                      | {todo}             | [datasheet](https://midsummerwholesale.co.uk/pdfs/samsung-gen-7-r290-datasheet.pdf) |
| Aira 6KW 1.0            | {MCS}         | 4.62     |  4.10    | 3.58     | R290 | MCS data `HP0372/06` | 2024-03            | [datasheet](https://cms-assets.prod.airahome.com/Installation_Manual_Aira_Outdoor_Unit_Rev1_1_UK_0dbf6a3a3c.pdf) |
| Viessmann 151.A06       | {todo}        | 4.58     | `4.10`   | 3.61     | R290 |                      | {todo}             | [datasheet](https://viessmanndirect.co.uk/files//7a81a248-e65a-4fcf-8735-e4a33fa33fe4/Energy%20Consumption%20Datasheet.pdf) |
| Mitsubishi Ecodan       | {todo}        | 4.62     | `4.08`   | 3.53     | R290 |                      | {todo}             | [site](https://library.mitsubishielectric.co.uk/pdf/book/EcodanR290Outdoor1#page-1) |
| Baxi  5Kw               | {todo}        | 4.77     |  4.06    | 3.39     | R32  |                      | {todo}             | [site](https://www.baxi.co.uk/new-build/products/air-source-heat-pumps/baxi-assure-hp50-ashp) |
| Daikin Altherma 4Kw     | {todo}        | 4.48     | `3.87`   | 3.26     | R32  |                      | {todo}             | [site](https://www.daikin.co.uk/en_gb/products/product.table.html/EDLA04-08E3V3.html) |
| Vaillant aroTherm+ 5Kw  | EN-14511      | 4.48     |  3.77    | 3.06     | R290 |                      | {todo}             | [datasheet](https://professional.vaillant.co.uk/downloads/aproducts/renewables-1/arotherm-plus/arotherm-plus-spec-sheet-1892564.pdf) |


><sup id="k_make">1</sup>`Make/Model` = models may cycle due to being oversized i.e. 8KW+
>
><sup id="k_std">2</sup>```NOT-DEFINED``` = SCOP standard unclear/old/NOT-DEFINED - results may be of question
>
><sup id="k_45">3</sup>```1.23``` = SCOP at 45C calculated as MEAN(35,55) when not made available in datasheet.
>      This produces conservative underestimate of SCOP when unavailable.

<div class="datatable-end"></div>

Changes:
- Fix data-entry error on Ebac 45C 4.63 to 4.38 (down to 4th)
- 2024-02 Ovum AC208P from `5.78` to `5.53` @ 35C, `4.15` to `4.00` @ 55C etc. [old-datasheet](https://www.ovum.at/wp-content/uploads/2023/10/ACP_Datenblatt_alle_Web_230928.pdf)
- 2024-02 EBac H1A05WG-GB from `5.11` to `4.91` @ 35C, `4.12` to `3.96` @ 55C  [old-datasheet](https://ebac-serverless.files.svdcdn.com/production/default/EBA%E2%80%A2230341_AIR-SOURCE-HEAT-PUMP-E-BROCHURE_HOT-WATER-CYLINDER.pdf?dm=1695277753) 
- 2024-04-25 Added Aira 6KW 1.0 with SCOP figures from MCS Product Database
