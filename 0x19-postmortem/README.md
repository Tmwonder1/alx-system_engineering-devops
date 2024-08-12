# Postmortem: Service Outage on August 10th, 2024

## Issue Summary

**Duration:**  
Outage lasted for 2 hours and 45 minutes from 10:30 AM to 1:15 PM EST on August 10th, 2024.

**Impact:**  
The outage affected 70% of our users globally. During this period, users experienced slow response times when accessing our main website, with page loads taking upwards of 30 seconds or timing out completely. Approximately 40% of users were unable to load the website at all.

**Root Cause:**  
The root cause was an unexpected server crash caused by a memory leak in the newly deployed version of the API service, which exhausted the available memory on the primary web server.

---

### Timeline

- **10:30 AM:** Issue detected via automated monitoring alerts indicating a significant drop in server performance and increased error rates.
- **10:35 AM:** DevOps engineer verified the alert and noticed a spike in memory usage on the primary web server.
- **10:40 AM:** Initial investigation focused on the load balancer, assuming the issue was related to improper traffic distribution.
- **11:00 AM:** The load balancer was ruled out as the cause, and attention shifted to the API service, suspecting a code deployment issue.
- **11:15 AM:** The issue was escalated to the API development team.
- **11:25 AM:** API logs were examined, revealing a pattern of increased memory consumption.
- **11:45 AM:** A memory leak in the recently deployed API service was identified as the likely cause.
- **12:00 PM:** The API service was rolled back to the previous stable version.
- **12:15 PM:** The primary web server was restarted, and system performance began to stabilize.
- **1:15 PM:** Full service was restored, and all monitoring metrics returned to normal levels.

---

### Root Cause and Resolution

**Root Cause:**  
The issue was caused by a memory leak introduced in the latest version of the API service, which was deployed the night before. The memory leak occurred due to improper handling of database connections in a new feature that was added to the API. Over time, this caused the primary web server's memory to be exhausted, leading to a crash that impacted the availability of the service.

**Resolution:**  
Once the memory leak was identified, the decision was made to roll back the API service to the previous stable version. This rollback removed the faulty code responsible for the memory leak. Following the rollback, the primary web server was restarted to clear the exhausted memory. The system was closely monitored after the rollback, and all performance metrics returned to normal.

---

### Corrective and Preventative Measures

**Improvements:**

- **Code Review Process:** The code review process will be enhanced to include more rigorous testing for memory management, particularly for changes involving database connections.
- **Monitoring Enhancements:** Improved monitoring will be implemented to detect memory leaks and abnormal memory usage patterns earlier, allowing for quicker identification and resolution of similar issues in the future.
- **Deployment Process:** A more cautious deployment strategy will be adopted, including phased rollouts and canary releases, to minimize the impact of future issues.

**Tasks:**

1. **Patch API Service:** Fix the memory leak issue in the new feature and ensure all related database connections are correctly managed.
2. **Add Memory Usage Alerts:** Implement additional monitoring on server memory to alert the team before critical memory thresholds are reached.
3. **Improve Rollback Procedures:** Develop and document a faster rollback procedure for critical services to reduce downtime in the event of a future deployment issue.
4. **Review Deployment Strategy:** Adjust the deployment strategy to include gradual rollouts with more comprehensive monitoring of early-stage deployments.

This postmortem highlights the importance of rigorous testing and monitoring, especially when deploying new features. The actions outlined will help to prevent similar incidents from occurring in the future and improve overall system resilience.
