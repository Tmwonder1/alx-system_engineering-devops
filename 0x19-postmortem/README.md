Postmortem: The Great Memory Leak of August 10th, 2024
Issue Summary
Duration:
Outage lasted for 2 hours and 45 minutes, from 10:30 AM to 1:15 PM EST.
(Or as we like to call it, the "Longest Coffee Break Ever").

Impact:
70% of our users were left hanging, staring at a spinning wheel of doom as our main website turned into a digital sloth. For 40% of those unfortunate souls, the website didn’t load at all, leaving them wondering if the internet had finally given up on them.

Root Cause:
Turns out, our API service was hogging memory like a teenager at an all-you-can-eat buffet. A sneaky memory leak in the latest deployment caused our primary web server to wave the white flag and crash.

Timeline (Or, How We Went from "It's Fine" to "Oh No!")
10:30 AM: Alert! Monitoring system tells us something is very wrong—like “the sky is falling” wrong.
10:35 AM: DevOps engineer chokes on coffee, confirms the alert. Memory usage is through the roof.
10:40 AM: "It’s probably the load balancer," we thought. We were wrong. Very wrong.
11:00 AM: Load balancer clears its name. Suspicion shifts to the API service.
11:15 AM: We bring in the API dev team, who are as thrilled as cats in water.
11:25 AM: API logs show a memory-hungry monster in our new feature. Mystery solved!
11:45 AM: We roll back the API service, like hitting Ctrl+Z on a bad decision.
12:00 PM: Server reboot—because when in doubt, restart it!
1:15 PM: Crisis averted, website returns to normal. DevOps engineer finally exhales.
Root Cause and Resolution
Root Cause:
In a nutshell, our shiny new API feature was like a bad roommate, leaving memory lying around everywhere. A missing database connection cleanup led to a memory leak that eventually exhausted the server’s memory, causing it to crash harder than a teenager after an energy drink binge.

Resolution:
We hit the rewind button and rolled back the API service to a previous, more civilized version. After a quick server reboot to clear out the clutter, everything was back to normal. The new feature is now on a timeout until it learns to clean up after itself.

Corrective and Preventative Measures
Improvements:

Code Review: We're beefing up our code reviews to spot memory leaks before they become memory tsunamis.
Monitoring: New memory leak detectors are on the way—because nobody likes surprises.
Deployment: From now on, we’re rolling out new features like they’re driving tests—slow and steady.
Tasks:

Patch API Service: Teach the API feature some manners—no more leaving memory all over the place.
Add Memory Alerts: Early warning systems for memory usage—because we'd rather not relive this nightmare.
Streamline Rollbacks: Make rolling back as easy as pressing undo.
Slow Down Deployment: No more pedal to the metal. We’re rolling out cautiously from now on.