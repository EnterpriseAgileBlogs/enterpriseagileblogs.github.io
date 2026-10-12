---
title: "Measuring velocity: Producing milk? Or shoveling shit?"
date: 2014-08-30T12:19:05+01:00
slug: measuring-velocity-producing-milk-or-shoveling-shit
translationKey: meten-van-productiviteit-melkproductie-of-poepscheppen
categories: ["Agile"]
tags: ["Actual velocity", "Measuring velocity", "Planned velocity", "Sprint backlog", "Sprint goals", "Techical Debt", "Velocity"]
original_url: https://3pro.wordpress.com/2014/08/30/measuring-velocity-producing-milk-or-shoveling-shit/
featured_image: "/images/blog/cow.jpg"
---

![cow.jpg](/images/blog/cow.jpg)

**Introduction**  
No, I’m not from the countryside, but my forefathers are, and I have farmers in the family. I have often used the metaphor of milk production when explaining measuring productivity in an agile environment. I encountered many teams in my coaching career that were firefighting. This indicates a poor delivered quality, and / or a high degree of technical debt in the product. You could say that teams work hard, but is all the work delivering value to the business product? I think so. But do we want to measure whether all activities performed are of added value to the business product? Or do we want to measure if a team adds real business value to the business product? I argue for the latter. There are plenty of teams that include a variety of peripheral activities in their product backlog, and consider this to count for productivity. And no, I do not offend a team when I say: No, these things do NOT count for productivity. Teams unmistakably work hard and sometimes even on weekends to be the hero. The fireman.

**Technical debt, poor quality and firefighting**  
Trend that I see is that in almost all businesses an enormous technical debt is built up. Up until the fact that the maximal boundary is reached or even crossed (almost all budget is going to maintenance, almost no budget left for innovation, while the business is screaming for faster Time to market!!!!). For me, this build up is largely caused by the project matrix organizations. Lack of ownership of applications, and teams under pressure from project managers with whips, cause that technical debt is steadily increasing in IT landscapes across the board (no project manager cleans up the mess from his predecessor (s)).  
The result is that Scrum teams (preferably fixed product teams with ownership of an application or sub-domain) are faced with solving production problems and tediously extensive impact analysis. This prohibits these teams to spend time on innovation (adding new features or modifying existing features (changes)). If a team is not able to reduce technical debt, or work on process improvement, the trend will be that the productivity (adding business value in terms of new features or modifying existing features) will decrease. This is shown in the following figure: 
![Trend without](/images/blog/Trend-zonder-en.png)

These teams will therefore produce less milk, and will have to shovel more and more shit every sprint. Result can be management teams deciding that Agile Scrum is ‘Not working’.

**Reducing technical debt and work on continuous process improvement will increase productivity in the long term**  
If you allow the shit to accumulate, it will be at the expense of milk production. Coaching teams to also reduce technical debt and work on process improvement in each sprint is essential. The coaching extends to Product Management, which has to be aware of the fact how much technical debt is in their product, and what it costs them NOT to reduce it. For this they need a proper insight in the extent of the technical debt. With the SQALE methodology on top of the open source tool SONAR each team will be able to periodically inspect the remediation time in man-days remaining in the application by the push of a button.

![SQALE](/images/blog/SCALE-dashboard.png)
 Example [SQALE](http://www.sqale.org/ "SQALE") dashboard with histogram divided into repair time (remediation cost) in man-days on:  
• portability  
• Maintainability  
• Security  
• Efficiency  
• Changeability  
• Reliability  
• Testability  
If Product management and team reach the state in which they consider planning reduction of technical debt and process improvement activities every sprint, then a temporary dip in productivity is to be expected. But in the long term this will be a ground for structural productivity increase. The first Toyota principle says: ‘Long-term concern over short term concern’. That also goes for creating a profound basis for increase of your productivity.  
This results in the following picture:
![Temporarily decrease](/images/blog/Trend-met-en.png)

You see, not only disposing of dirt, but also looking at the diet of the cows, the health of the cows, the speed in which the milking machine can be connected and disconnected, the way the barn is arranged, how effective the dirt is cleaned up, will lead to the eventual increase in milk production. All milk producing farmers will agree to this. This way of measuring productivity thus contributes to a potential to increase productivity on the one hand, and provides insight into the real business value added by the teams on the other!

**Sprint Planning: 4 backlogs!**  
Basically, for me, processing items from 4 backlogs will lead to a good sprint backlog:  
• The Product Owner is the owner of the Product or Team backlog with User Stories (New features, or changes on existing features).  
• The application or system architect owns and maintains a backlog of items in technical debt. Also broken up into small stories just like a Product Backlog, so that the items can be processed in one sprint.  
• The Scrum Master owns and maintains a backlog in with process improvement actions, which come from the retrospective sessions, prioritized by the team, based on which improvement story will deliver the greatest return to the team first.  
• The tester in the team owns and maintains the backlog of open production problems (please note, the backlog of open defects resulting from realization of actual User Stories is also there, but resolving those defects in the sprints will indeed count for productivity, as where resolving defects form versions already in production will not) .  
This results in the following visualization:

![Different backlogs](/images/blog/backlogs-en.png)

Keeping track of the extent to which teams perform these type of activities per sprint can be very useful for determining correlation between the degree of reduction of technical debt and performing process improvement activities, and the increase or decrease in productivity. This is empowering Product Management to be able to steer indeed!

**How do I want the realized velocity per sprint determined: the strict way!**  
As an Agile coach I am in favor of a clear and rigorous way of determining the realized productivity equally for all teams. It’s nice when each team is  determining their own way to count productivity, and many agile purists might agree. But in large organizations, with the establishment of a good agile governance and creating ways for product management to be able to direct better, standardization (yes, scary word!) is essential!  
These are my rules:  
• If a Story has not met the DoD, but work on the Story has taken off in the sprint, the Story points are NEVER counted again for both planned and actual velocity. This results in the sprint and release burndown never touching the zero baseline, but that does not matter.  
• A story on which work has not started yet in the sprint in planned in the next sprint, and points for the next sprint are counted for the planned velocity again (if the particular story is again planned by the PO).

Teams often agitate against this method of determining actual velocity. But it forces teams to try to reach the sprint goals every sprint. A team that decides if a Story is not completed to count half of the points in this sprint, and the other half in the next sprint, will quickly tend  to find it normal not to reach sprint goals. But what do we do to ensure that the finishing work on the Story is done in the next sprint? You plan the remaining tasks for that story in the next sprint. But that means that the planned velocity is lower, because less capacity is available for new Stories. As long as teams do not reach their sprint goals, the velocity will continue to fluctuate and will be unstable. This should be a drive for a team to improve.

**Epilogue**  
For the time being, there will a lot of shoveling shit going on in most companies. The awareness that the extent of technical debt in their application landscape, that requires heavy remediation, is huge, is now hitting many management teams. Do not think that problems arising because of the shit, are due tot the Agile initiatives! The Agile initiatives only make existing invisible shit visible. On the other hand, an agile way of working could be a means of structural, step by step, without big bang scenario, reduction of technical debt. As long as there is ownership of the products, and as long as we are measuring our milk production and have visibility and are able to steer upon that. The good thing for me as Agile coach is: there is tons of work to do in this area!…, and I love it!!
