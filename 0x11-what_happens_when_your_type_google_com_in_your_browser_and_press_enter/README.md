       +------------------+   DNS Resolution   +------------------+
       |                  | ------------------> |                  |
       |   Local Browser  |                    |   DNS Server     |
       |                  | <------------------ |                  |
       +------------------+                    +------------------+
                                      
                    |                                  |
                    |                                  |
                    v                                  v
        +------------------+               +------------------+
        |                  |               |                  |
        |   HTTPS Traffic  |               |    Server IP     |
        |                  |               |   (Port 443)    |
        +------------------+               +------------------+
                |                                  |
                |                                  |
                v                                  v
        +------------------+               +------------------+
        |                  |               |    Firewall      |
        |   Encrypted      |               |                  |
        |   Traffic        |               |                  |
        |                  |               |                  |
        +------------------+               +------------------+
                |                                  |
                |                                  |
                v                                  v
        +------------------+               +------------------+
        |                  |               |    Load Balancer |
        |    Load          |               |                  |
        |    Balancer      |               |                  |
        |                  |               |                  |
        +------------------+               +------------------+
                |                                  |
                |                                  |
                v                                  v
        +------------------+               +------------------+
        |                  |               |   Web Server     |
        |   Web Page       |               |                  |
        |   Serving        |               |                  |
        |                  |               |                  |
        +------------------+               +------------------+
                |                                  |
                |                                  |
                v                                  v
        +------------------+               +------------------+
        |                  |               |  Application     |
        |   Application    |               |  Server          |
        |   Server         |               |                  |
        |   Requesting     |               |                  |
        |   Data           |               |                  |
        |   from Database  |               |                  |
        |                  |               |                  |
        +------------------+               +------------------+
