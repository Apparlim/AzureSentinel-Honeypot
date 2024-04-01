# 🧑‍💻 AzureSentinel-Honeypot
• Implemented an advanced honeypot solution to proactively detect and analyze potential security threats, enhancing overall system resilience.

![image](https://github.com/Apparlim/AzureSentinel-Honeypot/assets/142485188/f07fc134-7b46-475c-a292-9718ca8f6ef4)


<h1>🤖 Installation Instructions </h1>
<h2> Requirements</h2>
• An active Microsoft Azure account.

• Basic knowledge of VM ( Virtual Machine) and networking in Azure.                                                          
 • SSH client (e.g.., Putty) installed on your local machine.      
 
<h2> Step 1: Set Up Azure Virtual Machine (VM) </h2>
                                                                                                                      
 <h4>•Log in to Azure Portal: </h4>                                                                                                     
                                                                                                                             
                                                                                                                           
 Go to Azure Portal ( https://azure.microsoft.com/en-us) and sign in.                                 






 <h4> • Create a New VM:  </h4>                                                                                                      
                                                                                                                    
•Navigate to the "Virtual machines" section and click on "Create" and after that "Virtual machine".                           
• Fill in the necessary details like subscription, resource group, VM name, region, etc.                                             
• Select Debian as the operating system image.                                                                                   
• Choose the appropriate size for the VM based on the expected load.                                                                  
• Go to the additional options like disks, networking, management, and advanced settings.                                    
                                                                                                                            <h4> • Networking Setting  </h4>  
                                                                                                                            
• Ensure that the network security group (NSG) attached to the VM's network interface has a rule to deny all inbound traffic 
  which you can adjust based on your network policy.                                                                                                                                                                                                                                             
 • Make sure on allowing specific ports that are necessary for the honeypot operation and management.                                                                                                                      
 <h2> Step 2: Install and Configure the Honeypot</h2>
 
<h4> Access the VM:</h4>

 • Once the VM is set up, obtain its public IP address from the Azure portal.
• Open Putty and connect to the VM using its IP address .

<H4> Install Honeypot Software:</H4>

• After accessing the VM via SSH, update the package list: sudo apt-get update                                                                                               
                                                                                                                                                                            • Install any required dependencies for the honeypot software.                                                                                                                
                                                                                                                                                                            • Clone the AzureSentinel-Honeypot repository or download the latest release to your VM.                                                                                                                                                               
• Navigate to the downloaded or cloned directory: cd AzureSentinel-Honeypot.                                                                                                          
• Follow theSpecific instructions to complete the installation of the honeypot.

<h2> Step 3: Verify Installation</h2>

<h4> Start the Honeypot Service: </h4>

• From within the project directory, start the honeypot service. This could be through a script or command specific to the honeypot you are using.                              
• Ensure that the service is running correctly and listening on the specified ports.

<h4> Test the Honeypot:</h4>

• Run an attack or use a testing tool to verify that the honeypot is capturing and logging activities as expected.

<h4> Step 4:Post-Installation Setup </h4>

• Configure any additional settings for monitoring, alerting, or integrating with Azure Sentinel for enhanced security analytics and threat management.


<h2> Diagram </h2>

![image](https://github.com/Apparlim/AzureSentinel-Honeypot/assets/142485188/728e5c66-611c-4576-b2fb-0c4620df671b)



<h1> 🛠️Tools used </h1>
• Microsoft azure 

• Virtual Machine  
• Potty    


 <h1>🎆Achievements </h1>
• Deployment Success: Successfully implemented a sophisticated honeypot using a custom framework.

• Intrusion Detection: Detected and logged various intrusion attempts, gaining insights into potential threats.     
• Unauthorized Access: Demonstrated the effectiveness of the honeypot in preventing unauthorized access to the system.    
• Attack Analysis: Conducted in-depth analysis of captured attack data, providing valuable intelligence for security enhancement.

<img width="950" alt="Screenshot 2024-02-22 235105" src="https://github.com/Apparlim/AzureSentinel-Honeypot/assets/142485188/ab952db5-f04b-42e9-adce-04a28255fee8">

<h1>Disclaimer</h1>
⚠️ Note:
• Ensure proper authorization before deploying honeypots in any environment.

<h1>Result</h1>

<img width="960" alt="Screenshot 2024-02-22 235731" src="https://github.com/Apparlim/AzureSentinel-Honeypot/assets/142485188/af1f1b1d-e9dc-4bc7-bdf2-0d44ea4e53e4">


<img width="944" alt="Screenshot 2024-02-23 000731" src="https://github.com/Apparlim/AzureSentinel-Honeypot/assets/142485188/dd59172b-bb43-42a6-a93e-a3112790800f">



<img width="960" alt="Screenshot 2024-02-23 000347" src="https://github.com/Apparlim/AzureSentinel-Honeypot/assets/142485188/65f35558-0948-43f2-9a3d-86e8f7b8c4b1">



## License

This project is licensed under the MIT License - see the LICENSE file for details.

