---
title: "From Scrum team to agile organization (Part four)"
date: 2014-05-14T12:23:09+01:00
slug: from-scrum-team-to-agile-organization-part-four
translationKey: van-scrum-team-naar-agile-organisatie-deel-4
categories: ["Agile"]
tags: []
original_url: https://3pro.wordpress.com/2014/05/14/from-scrum-team-to-agile-organization-part-four/
featured_image: "/images/blog/Structureshift4.png"
---

**Agile maturity step 4: DevOps within IT**  
**Introduction**  
In my blog about Agile maturity step 3: ‘Working in physical product teams, possibly supplemented by virtual Ops‘ I explained that it works more efficiently if you reorganize the IT to specific business domains or business products. Such a reorganization supports utilization and implementation of the Scaled Agile Framework optimally, and increase of productivity of 50 % is easily achievable, when implementation is done adequately.

The next step is a step which many large organizations can not easily make, and is again a structural change. We are going to merge the mirrored operations staff with the development staff (as far as they are mirrored). This will result in many issues for large organizations, which I will discuss here. Many organizations will stop at agile maturity step 3, and I encourage every IT organization to strive for that level. Most IT organizations are already far past the point where they have the luxury of saying ‘we will keep working like we did for the past 30 years’. The technical debt is steadily increasing and is showing unsustainable proportions in most organizations I encounter, while the demand for a faster ‘time to market’ increases further.  
Below for reference development stages one more time in a row :  
1 .Working iteratively within (temporary) projects in a matrix organization  
2. Working in virtual product teams, assembled from functional oriented departments  
3. Working in physical product teams , possibly supplemented by virtual Ops  
4. DevOps within IT  
5 . Company-wide product or domain teams

This is the 4th blog in a series of 5, on the 4th agile maturity step.

**The 4th step is another organizational change, but also leads to an ‘Organizational Culture Shift’.**  
The fluency model of James Shore and Diana Larsen (See Figure 1.) shows a different view on working towards a complete agile organization. You could say that working iteratively in projects is similar to the Start: ‘Building Code’ of this model, which leads to a ‘team culture shift’.  
Maturity step 2 works towards ‘focus on value’, by assembling virtual product teams. This should lead to a ‘skill shift’ for those teams.  
![Fluency model](/images/blog/fluency-model.jpg)
  
Figure 1 : The model of fluency James Shore and Diana Larsen

In maturity step 3 we move towards ‘Deliver Value’. This results in an organizational structure shift. We are going to create domain or product departments within the IT organization. Within these domain or product departments one or more agile delivery teams, or fixed (sub)product teams are positioned in release trains.  
In maturity step 4 we move towards ‘Optimize Value’. Fixed DevOps teams measure their productivity and become more predictable. Belonging to a fixed team with one HR responsible manager gives a better intrinsic motivation for delivering quality software. Predictability at release level is achieved here, including deployment through Ops . The result is an even better view on portfolio level when certain Epics could be deployed to the market. But also a better understanding on how to utilize the resources in the fixed teams and thus, having a more efficient portfolio management. Which Epics do we develop, which ones will we skip, what will deliver most business value to our company.

In fact, we are talking about a total tilt from a complex organization with simple tasks towards a simple organization with complex tasks. It is precisely these complex tasks, combined with an increasing responsibility lower in the organization, that will increase the quality of work. Indeed, a culture change! This requires a lot from employees, but also from managers ( Kuipers, Amelsfoort & Kramer (2010): ‘The new organization’).

**Agile maturity step 4: DevOps within IT**

![step 4](/images/blog/step-4.jpg)
  
Figure 2 . The IT domain consists of departments in which fixed DevOps teams are responsible for development, maintenance and operation of (sub) business products.

It is of course possible, and also mentioned in blog part three, to virtually add people from operations to fixed product teams. In this case we go one step further and bring the operations people under the same management and HR responsibilities as the development staff. In both cases, hand-offs can be eliminated, as can be read under ‘Optimize Value’ in the model of Shore and Larsen. Eliminating these hand-offs is nicely illustrated in the figure below by Matt Watson. The additional benefit that having only one manager responsible for development and operations brings is that his interest will be having an optimal process. What may clash is that Development and Operations often have different interests. But in the end it’s all about delivering business value of good quality fast.  
![DevOps](/images/blog/devops.jpg)
  
Figure 3. From Matt Watson, stackify.com, shows that the hand-offs between development and operations are eliminated when organizing in fixed DevOps teams.  
![operations department example](/images/blog/operations-department-example.jpg)
  
Figure 4 . Example operations department of a large company.

Operations departments in some cases are mirrored to the development departments, but can also be organized completely different. The above example of an operations department of a large company indicates how many sub-departments can exist, each with their own specialty and coordination complexity. And in particular this coordination complexity will cause viscosity within an organization, and will stretch lead times for deployment. Coordination requires a lot of indirect capacity, which could be used to fill in the gaps (after re-structuring of the organization, re-training, re-acquisition and re-positioning of personnel) for direct development capacity when creating fixed teams.

![indirect to direct](/images/blog/indirect-to-direct.jpg)
  
But this brings many challenges. You can imagine that if you want to allocate a specialized department of 5 people to 30 fixed product teams, this is difficult.  Also products will often use many more platforms than just one. How will you deal with the formation of DevOps teams? Often there is an acquisition stop for the recruitment of new staff. And you can not slice up individual specialists, who are already hard to find for some platforms.

In short, there is no simple solution for this step in maturity. For small organizations, it will be easier to create fixed DevOps teams. For larger organizations this still brings too much challenges. It’s a good start to involve operations employees in the fixed product development teams as described in step 3 (Virtual Ops). From there management can start to identify how to reduce the coordination capacity (reduction of indirect staff ) of the many operations departments. Also they can change the attitude of the operations departments into thinking more business product-oriented, instead of just thinking in their own specialism. Doing so, management of both development and operations departments should carefully weigh the combinations of interests that they have, such as faster ‘time to market’, ‘Customer intimicy’, ‘Operational Excellence’ and  ‘intrinsic motivators’.

**Advantages and disadvantages of Agile maturity step 4:**  
The same advantages and disadvantages of step 3 apply to step 4. The advantages and disadvantages specific to step 4, in addition to those of step 3, are highlighted in italic.  
**Advantages:**

1. *Direct involvement of operations staff in the agile process from impulse to deployment.*
2. *DevOps teams take better account for non funcional requirements for deployment.*
3. Reduction of overhead for management, planning, directing and *coordination*.
4. Reduction of effort for project-related documentation (Project Plans, Requirements Management plans, Configuration Management plans, Test plans, etc., do not have to be produced​​, or only maintained and not produced ​​from scratch for each project).
5. Reduced effort for domain related documentation (Vision Documents, Domain Models, Use Case Models, SAD’s, Supplementary Specs and Designs are often initiated per project, and thrown away at the end. Now they only need to be maintained per product). Now some (misinformed) agilists will say why document? I am convinced that good requirements, domain and design documentation is key for mission-critical products. For that, RUP artifacts are a good basis. Building a temporary campaign site?, then you can refrain from producing documentation indeed.
6. Fixed *DevOps* teams are a breeding ground for intrinsic motivation.
7. Fixed *DevOps* teams can build on domain knowledge.
8. Fixed *DevOps* teams can build on a reference for predictability.
9. Fixed *DevOps* teams can continuously (rather than temporarily for a project ) work on process and productivity improvement.
10. Fixed *DevOps* teams will feel responsible for the overall quality of a product, not only for the scope of a temporary project (The whip of a project manager in a temporary project team leads to taking short cuts on quality, and thus, to increase of technical debt in IT landscapes. This is a trend, and the amount of technical debt in most large organizations has grown to irreversible proportions).
11. No repetition of actions every time a project for innovation on a specific product is initiated (Staffing, making plans, getting environment up and running, initiating a steering committee and so on).
12. Test environments are permanently kept in the air versus letting them be broken down and built up per project.
13. A single HR manager responsible for the *DevOps* teams gives clarity and a sense of belonging.
14. There will be less ‘pulling’ and ‘moving’ of staff between teams. Changes in staffing are more analog to the movements of a supertanker, rather than spreading your weekly effort across multiple projects. So, staffing *DevOps* teams in the long term is more slowly adjusting to the growth or decline or differentiation of the Portfolio backlog.

**Disadvantages:**

1. *For large IT departments it will be difficult to allocate operations staff to physical DevOps teams. This requires extensive reorganization, retraining, re-acquisition and re-distribution of responsibilities.*
2. *There will be more need for automated deployment, this often requires investments.*
3. In a pilot with *DevOps* teams, resourcing will be a problem. Specialists are often scarce and management is not easily inclined to hire additional staff. What they have to realize is that, when scaling up, many indirect coordination staff can be released, leaving room for hiring more direct specialist staff.
4. Configuration management issues will occur when multiple *DevOps* teams in the same application layer have to implement features for ‘their’ business product.
5. For large IT landscapes issues will arise about the creation of component or feature teams, and coordination of the synchronization of content of the backlogs for those teams has to be solved.

**In terms of percentage on Return on Investment his step will get a 100%.**  
In Part 5 of this series, I ‘m going to talk about Agile maturity step 5: Company-wide product or domain departments: back to decentralization and silos ! With also attention to holocracy, sociotechnology, and the de-centralization / centralisation waves of IT departments.

With many thanks to Jasper Doornbos, for his contribution to this part, by reviewing on scientific correctness and foundation.
