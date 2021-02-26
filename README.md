# CoguLog
The CoguLog project it's a very simple way to implement complete tools for logging to your application, the principal idea for the project is create a new standard for logs, in an optimized way taking up little space and having a high logging speed.

## Log Levels
The project use simples log levels but the CoguLog have built-in sub levels
- 0 Fatal
- 1 Error
- 2 Warning
- 3 Info
- 4 Debug
- 5 Trace
- 6 Security
  - 61 Foreign access info
    - 611 Accepted Connection
      - 6111 Save log with IP
      - 6112 Save log without IP
    - 612 Droped Connection
      - 6121 Save log with IP
      - 6122 Save log without IP
