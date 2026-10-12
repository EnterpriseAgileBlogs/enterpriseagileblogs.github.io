---
title: "From Scrum team to agile organization (Part three)"
date: 2014-04-14T16:13:56+01:00
slug: from-scrum-team-to-agile-organization-part-three
translationKey: van-scrum-team-naar-agile-organisatie-deel-3
categories: ["Agile"]
tags: ["domain departments", "intrinsic motivators", "physical product teams", "scaled agile framework"]
original_url: https://3pro.wordpress.com/2014/04/14/from-scrum-team-to-agile-organization-part-three/
featured_image: "/images/blog/Structureshift3.png"
---

**Agile maturity step 3: Working in physical product teams , possibly supplemented by virtual Ops**

**Introduction**  
In my blog about Agile maturity step 2: ‘Working in virtual product teams, assembled from functional oriented departments‘, I explained the pros and cons of putting together fixed teams from different departments. This is already a first step in leaving the whole project paradigm, and move towards a more product -oriented way of working . Because people have different bosses or managers in this situation, the exact assignment or role might be fuzzy to people. Although the return on investment is already higher in this situation, it is still better to migrate to fixed product teams. However, this requires an organizational change, and that’s easier said than done.  
Below for reference development stages one more time in a row :  
1 .Working iteratively within (temporary) projects in a matrix organization  
2. Working in virtual product teams, assembled from functional oriented departments  
3. Working in physical product teams , possibly supplemented by virtual Ops  
4. DevOps within IT  
5 . Company-wide product or domain teams

This is the 3rd blogpost in a series of 5, on the 3rd step of agile maturity.

**3rd step of agile maturity leads to organizational change**  
The fluency model of James Shore and Diana Larsen ( See Figure 1 . ) Shows a different view on working towards a complete agile organization . You could say that the iterative working on temporary projects is similar to the ‘Start : Building Code’ of this model, which leads to a ‘team culture shift’.  
Maturity step 2 works towards ‘focus on value’, by assembling virtual product teams. This should lead to a ‘skill shift’ for those teams.  
![Fluency model](/images/blog/fluency-model.jpg)

Figure 1 : The fluency model by James Shore and Diana Larsen

In maturity step 3 we move towards ‘Deliver Value’. This results in an ‘Organizational structure shift’. We are going to create domain or product oriented departments within the IT organization. Within these domain or product departments one or more fixed agile delivery (Scrum) teams are working on certain (sub)products.  
Because the teams in the previous step have been working on their skills in virtual product team formation, it is now time to harvest the benefits from that. With the accumulated skills (see blog part two), and only having to report to one manager, a fixed team can be predictable and loose the fire fighting culture. Eliminating technical debt and improve automation through continuous process improvement will result in a faster time to market (increase productivity) and a better quality product. This results in the delivery of more (business) value to the organization.  
So, transform the virtual teams to reside in domain or product oriented departments, having only one HR responsible manager with focus on innovating and maintaining a certain business product. These departments will be responsible for a predictable delivery, along with the quality of the product.

![Step 3](/images/blog/step-3.jpg)

Figure 2: Agile maturity step 3: Working in physical product teams , possibly supplemented by virtual Ops

A model that is supported very well by fixed product teams, organized in domain departments, and can thus be used as a reference model for scaling agile, is the ‘Scaled Agile Framework ®’ or ‘SAFe™’ by Dean Leffingwell.

But whether or not you support SAFe as a reference model for scaling agile, or you support the more Scrum of Scrum alike models from Graig Larman and Bas Vodde (<http://www.crosstalkonline.org/storage/issue-archives/2013/201305/201305-Larman.pdf>), they both are mostly supported by fixed product teams, organized into (sub) domain or (sub) product (or product area, as Larman and Vodde define it) departments.

![TheBigPictureSAFe](/images/blog/thebigpicturesafe.jpg)
  
Figure 3: The ‘Scaled Agile Framework ®’ or ‘SAFe™’ by Dean Leffingwell

The Portfolio level of this model represents the business side of the organization. The program level can be a physical domain or product department (See the discussion I started in the LinkedIN group of Scaled Agile Framework about the fact that the term program level, to me, is confusing). The team level represents the agile delivery teams, having responsibility for (sub)products within the domain or product department.  
What you see in this model is that the flow of requirements , from impulse to production, is supported by three levels of backlogs. These contain from coarse to fine: Epics (span releases), Features (fit within releases) and User Stories (fit within sprints or iterations).  
Also mentioned is the combination of the use of lean and agile principles. The teams work iterative, while the flow of requirements is optimized using lean principles.  
You could already implement this model using virtual teams, as described in step 2, but the chance that these teams remain stable, which is essential for this model, is less than when the resourcing is the responsibility of one department manager, who also is responsible for the quality of the product.

**Advantages and disadvantages of Agile maturity step 3:**  
**Advantages:**

1. Reduction of overhead for management, planning, directing and coordination.
2. Reduction of effort for project-related documentation (Project Plans, Requirements Management plans, Configuration Management plans, Test plans, etc., do not have to be produced​​, or only maintained and not produced ​​from scratch for each project).
3. Reduced effort for domain related documentation (Vision Documents, Domain Models, Use Case Models, SAD’s, Supplementary Specs and Designs are often initiated per project, and thrown away at the end. Now they only need to be maintained per product). Now some (misinformed) agilists will say why document? I am convinced that good requirements, domain and design documentation is key for mission-critical products. For that, RUP artifacts are a good basis. Building a temporary campaign site?, then you can refrain from producing documentation indeed.
4. Fixed product teams are a breeding ground for intrinsic motivation.
5. Fixed product team can build on domain knowledge.
6. Fixed product team can build on a reference for predictability.
7. Fixed product team can continuously (rather than temporarily for a project ) work on process and productivity improvement.
8. Fixed product team will feel responsible for the overall quality of a product, not only for the scope of a temporary project (The whip of a project manager in a temporary project team leads to taking short cuts on quality, and thus, to increase of technical debt in IT landscapes. This is a trend, and the amount of technical debt in most large organizations has grown to irreversible proportions).
9. No repetition of actions every time a project for innovation on a specific product is initiated (Staffing, making plans, getting environment up and running, initiating a steering committee and so on).
10. Test environments are permanently kept in the air versus letting them be broken down and built up per project.
11. A single HR manager responsible for the product teams gives clarity and a sense of belonging.
12. There will be less ‘pulling’ and ‘moving’ of staff between teams. Changes in staffing are more analog to the movements of a supertanker, rather than spreading your weekly effort across multiple projects. So, staffing product teams in the long term is more slowly adjusting to the growth or decline or differentiation of the Portfolio backlog.

**Disadvantages:**

1. In a pilot with a couple of virtual product teams, resourcing will be a problem. Specialists are often scarce and management is not easily inclined to hire additional staff. What they have to realize is that, when scaling up, many indirect coordination staff can be released, leaving room for hiring more direct specialist staff.
2. Configuration management issues will occur when multiple product teams in the same application layer have to implement features for ‘their’ business product.
3. For large IT landscapes issues will arise about the creation of component or feature teams, and coordination of the synchronization of content of the backlogs for those teams has to be solved.

Last year I was responsible for the implementation of the program and team level, using SAFe as a reference model, within a client organization. And I say reference model, because each customer has a specific situation. For example I used Use Case Slices as defined in Use Case 2.0 by Ivar Jacobson, in stead of User Stories, as a unit for the team backlog on team level. This because the organization already worked with Use Case Models. Also, because this organization produces quality products for implementation by partners, they continued to use the RUP documentation standards for definition of requirements and design documentation.  
The IT organization is indeed reorganized from functional departments to four physical product or domain departments. Within these product departments one manager is responsible for both HR and staffing of the product teams, and  the quality of the products  maintained by his department! They totally left the project silo paradigm, and the role of project manager transferred into the role of delivery manager, overseeing and coordinating delivery of releases every PSI period, involving all required departments.

This creates a totally different set of dynamics. People belong to a product group (see intrinsic motivator ‘Purpose’ in Part two), people are given room for decisions on quality improvement as a team (Autonomy) and space for process improvement (Mastery).

It also brings a lot of challenges. For example, it is hard when a culture is still entirely focused on project thinking, and the governance is organized accordingly. Also, there is no culture of process improvement, because people are used to projects always being under time pressure. So they are used only to work on the product, not on the process. Problems also arise with organizing into fixed teams responsible for maintenance and innovation of a product. This is a complete paradigm shift for people who are used to multiple (temporary) project teams on innovation, and one maintenance team for a specific product. And what about the maturity of the organization, the competences required from employees, and the alignment with the processes on the business side.

This shows that this is a huge step for any organization. But when I look at the trend that technical debt only increases in IT organizations thinking in the traditional project silo, while the demand for a faster ‘Time to Market’ is only increasing, this might be a necessary step for most organizations!!!

**In terms of percentage on Return on Investment for this step, I give it a 50%.**

(see also the benefits that customers already encountered after implementation of the Scaled Agile Framework, download the foundations presentation at <http://www.scaledagileframework.com>).

In part four of this series, I ‘m going to talk about Agile maturity step 4: DevOps within IT
