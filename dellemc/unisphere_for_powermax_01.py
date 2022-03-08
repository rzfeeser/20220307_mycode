#!/usr/bin/python3
"""Alta3 Research | RZFeeser@alta3.com
   Using DellEMC PyU4V client for management of PowerMax Storage Arrays via RESTful API requests to Unisphere.

   PyU4V - Client for PowerMax Storage Array
   GitHub @ https://github.com/dell/PyU4V/

   Per GitHub README.MD:
   PyU4V is a Python module that simplifies interaction with the Unisphere for PowerMax REST API. It wraps REST calls with simple APIs that abstract the HTTP request and response handling.

   Requirements:
   - Install PyU4V REST client:
     python3 -m pip install PyU4V
"""

#python3 -m pip install PyU4V
import PyU4V

def main():
    """run-time"""

    # Initialise PyU4V connection to Unisphere
    conn = PyU4V.U4VConn()

    # Perform a system health check, this call can take 15-20 minutes to
    # complete in Unisphere due to the nature of the checks performed
    conn.system.perform_health_check(description='test-hc-dec19')

    # Get details of the last system health check
    health_check = conn.system.get_system_health()

    # Get a list of physical disks installed in the array
    disk_list = conn.system.get_disk_id_list()
    # Get disk information for each disk installed
    for disk in disk_list.get('disk_ids'):
        disk_info = conn.system.get_disk_details(disk_id=disk)

    # Close the session
    conn.close_session()

    # dir(health_check)
    # type(health_check)

    # type(disk_info)
    # dir(disk_info)


if __name__ == "__main__":
    main()
