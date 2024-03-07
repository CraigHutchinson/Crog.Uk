---
layout: post
title:  "Are ASHP datasheets reliable?"
date:   2024-03-07 16:11:00 +0000
categories: HeatPump
---

This is an open question of mine, questions the datasheet SCOP figures for many products.  

Firstly, it appears some manufacturers are very active and update their performance figures. 
The one place we have to verify is the [MCS Product database](https://mcscertified.com/product-directory/) 
which provides 3rd party verification and correlation here is our key indicator of data reliability.

 `Ideal Heating` (and others TBC) are not showing the verified figures on their website,
 either due to compilcated internal processes or lack of desire to show a public image with lesser performance.


**This is our concern as to how we know what numbers to trust?**

So, in need of picking an example, I will take `Ideal Logic Air 5kW` as a basis of what appears to 
be over-stated SCOP on the marketing site and donwloadable datasheet! 

| Data Source                        | SCOP@35C | SCOP@45C | SCOP@55C | Link |
| ---------------------------------: | :------- | :------- | :------- | --- |
| Site+Datasheet                     | 5.07     | N/A (`4.36` est.)     | 3.65        | [Datasheet](https://idealtouch.co.uk.idealboilers.com/uploads/documents/230620_Logic_Air_Spec_Sheet_RevB_Web.pdf)  |
| MCS cert. `KIWA 00027/023 HP`      | 4.39     | 3.83     | 3.06     | [MCS Product Database](https://mcscertified.com/product-directory/) |
| **Discrepancy**                      | **+0.68**   | **+0.53**    | **+0.59**    | |

I get that they want to make things look good but this could be misleading consumers and as a community we
 may need to find how we raise this.

For me, here we will need to include MCS correlation in our product databse to have higher confidence in the figures, 
there is a lot to verify and digest here.

**Current list of verified devices that match third-party MCS verified SCOP performance:**
- Ebac 5Kw
- Vaillant 5Kw
