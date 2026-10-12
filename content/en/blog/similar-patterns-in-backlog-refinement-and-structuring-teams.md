---
title: "Similar patterns in backlog refinement and structuring teams"
date: 2018-01-14T11:47:00+01:00
slug: similar-patterns-in-backlog-refinement-and-structuring-teams
translationKey: vergelijkbare-patronen-bij-backlog-refinement-en-structureren-van-teams
categories: ["Agile organization structure", "Agile requirements", "Enterprise agility", "Product orientation", "Scaling agile", "Value streams", "Business agility"]
tags: []
translated: true
featured_image: /images/blog/wordcloud-engineering.jpg
---

![wordcloud-engineering.jpg](/images/blog/wordcloud-engineering.jpg)

'From thinking in solutions to thinking in customer needs' and ‘From thinking in the layout of the IT landscape to thinking in value streams’

## **Introduction**

Every time I come into contact with new teams and new organizations that are used to working the traditional way, I also come across habits that are hard to break. People in IT have been used to working in a certain mode and structure for so many years that it has become very difficult to undergo the paradigm shifts that are needed to become agile as an organization, let alone as a team. In an earlier blog I already listed a number of paradigm shifts (</en/blog/paradigm-shifts-in-scaling-agile/>), and here I talk about just two of those paradigm shifts: 'from thinking in solutions to thinking in customer needs' and ‘from thinking in the layout of the IT landscape to thinking in value streams’

## **Scrum**

Of course it seems easy to have a team trained in Scrum and then get started. Preferably under the guidance of an experienced coach. Scrum seems easy to apply, but if you have a history of working traditionally, much more discipline and change is necessary than you would expect. That goes for team members as well as their management.

## **Backlog refinement and thinking in business value**

One of the most underestimated things I come across, especially with architects and engineers, is thinking in business value. Thinking in business value means letting the effectiveness of the whole prevail over the efficiency of the parts. What I mean by this is that architects and engineers are used to thinking in technical components. Technical components are part of the SOLUTION and do not necessarily represent business value. In fact, they usually do not. Architects and engineers think: 'If I am editing this code, I might as well edit the code for the next User Story, because it is in the same component. Why would I build and deploy this Story, if I have to check in the same code again for the next Story?'. This is thinking in efficiency, not in effectiveness. If we visualize this in a simple way, it looks like this:

![req1.png](/images/blog/req1.png)

![Figure 1 and 2: Components within 1 application with changes per component](/images/blog/req2.png)

*Figure 1 and 2: Components within 1 application with changes per component*

Above you see that component after component is changed, regardless of whether these changes independently represent business value. A phenomenon you often see with starting Scrum teams is that their backlog is filled with this kind of technical ‘changes’. However, the backlog items should be 'cut' or ‘sliced’ differently. In backlog refinement we should define customer needs as much as possible, and not technical work. After all: a Product Owner must come from the business, and that same person must draw up the backlog. As a rule this person has no understanding of technical matters, and then cannot prioritize the backlog either!

Below you see visualized how the work should be ‘sliced’ instead (assuming a feature for this application could be put into production independently):

![Image with screenshot Automatically generated description](/images/blog/req3.png)

*Figure 3: ‘slicing’ features right through multiple components of an application*


This is what the Scrum guide says about backlog items: '*The Product Backlog lists all features, functions, requirements, enhancements, and fixes that constitute the changes to be made to the product in future releases'*.

The guide does not specifically mention User Stories as the prescribed format. Different formats are allowed. But using the User Story format is a very common ‘practice’ and it forces teams to think in business value. And in practice this turns out to be quite difficult.

'As a \<stakeholder\> I want \<customer need\> so that \<business value\>'. This format is very powerful. It forces teams to think about the end user/customer: who is that? It forces teams to think in the context (needs) of the customer and the business value it will deliver for that same customer.

**Story mapping as an aid to thinking in business value**

In practice it turns out to be very tough to teach this correct ‘slicing’ behaviour. As a coach I keep reminding the teams of the need to deliver business value frequently. The instrument I often hand them is Story Mapping. In my experience Story Mapping is the most powerful instrument to get teams thinking in business value, customer journeys, minimum viable products and so on. But even then it often takes periods of 3 to 6 months before teams really understand the power of this instrument. Backlog refinement is not simple, and it is too often thought of as simple. As long as the organization works with component teams (teams responsible for innovating and maintaining 1 or a few applications, instead of a business product) it is even harder to teach teams this, because backlog items for only one application do not necessarily represent business value; usually they do not. Let alone that the product owner can define work for the team in terms of business value..

**Pattern that emerges when introducing agile working enterprise-wide**

Since 2013 I have been helping organizations achieve their business objectives by using elements of ‘scaling agile’, in particular the ‘Scaled Agile Framework’. The phenomenon I describe above I have since experienced as a recurring pattern. However, I saw the same pattern recurring at the organization (structure) level too! Take a look with me:

The enterprise IT landscape usually looks something like this (simplified):

![Image with screenshot Automatically generated description](/images/blog/req4.png)

*Figure 4: The layers of the IT landscape*


The IT landscape is layered horizontally, according to the strategy of converging the landscape to fewer applications per layer in order to reduce the total cost of ownership. Teams are traditionally oriented towards one of those layers. In the front office you see many web and app teams, and in the back office you see many teams maintaining the legacy applications. Again, this is more than simplified and very general. Here you initially see component teams being ‘glued’ onto the three layers:

![Image with screenshot Automatically generated description](/images/blog/req5.png)

*Figure 5: Component teams are positioned on the three layers of the IT landscape*


In a scaled environment we want teams that orient themselves on a business product, or value stream as we call it. Examples of the main value streams for an insurance company are: Property & Casualty, Life and Pension insurance. But the customer needs for these product (group)s usually have an impact on front, mid and back office. We also no longer have projects. The scope of the projects is defined in so-called Epics, and we bring these to the fixed teams of teams. Another paradigm shift I often talk about. Epics are large customer requirements that should also independently represent customer value, and not just an arbitrary assignment. And each value stream uses certain applications from each layer. This looks as follows:

![Image with screenshot Automatically generated description](/images/blog/req6.png)

*Figure 6: Teams of teams oriented on a business product (group) or value stream cut right through the three layers of the IT landscape*


Here you see that teams traditionally specialize in a certain technology or technical layer. Instead, they should organize into feature teams or tribes that specialize in a certain business product, or sub-business product. How can someone be product owner if the team maintains only one application? Which business product is she then the owner of?

In essence this blog says: 'stop thinking horizontally, and start thinking vertically!'. Or in other words: filling a backlog is not as simple as one might think when you start as product owner. That is why I advise all disciplines involved in some form of analysis to become acquainted with agile requirements engineering. There is much more to discover than just the User Story practice and story mapping. Use-Case 2.0 by Ivar Jacobson, for example, is another practice, and there is more.

If this blog comes across as too complex, you understand why a lot of training and coaching is needed (also, and especially, for management) to bring about all the necessary paradigm shifts. And with this I am only touching the tip of the iceberg of the dozens of paradigm shifts.

I hope the pattern is recognized. And yes, these are enormous challenges. Both ‘slicing’ backlog items the right way (so not component-oriented, but customer-value-oriented) and organizing teams at product level instead of per layer (or application) in the IT landscape. What about configuration management, resourcing and a flexible IT landscape? These are things that are not all simply arranged. In fact, at most companies the IT landscape is still far from flexible. So we will probably keep encountering the combination of feature and component teams for the time being. In a next blog I will therefore go further into this pattern of component-wise orientation versus feature / value stream orientation. </en/blog/fractal-structure-patterns-when-scaling-agile-enterprise-wide/>
