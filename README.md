# ctf

#First Time
Step 0) Have the latest virtualbox(www.virtualbox.org) installed and the latest vagrant(www.vagrantup.com) installed.

Step 1) In terminal,inside the ctf-master:

		$vagrant up --provider virtualbox

Step 2) Go to 127.0.0.1:8080 in the browser

Step 3) (If it is first time using 'vagrant up') Register with the site

Step 4) To start site & servers,

		$vagrant ssh (does not work on windows-use program like putty)

		$devploy (if not the first time running system)
		
		$launch

#If install fails (IMPORTANT)
	If the install fails,
		1) $vagrant destroy

		2) Delete directroy that you tried to vagrant up in

		3) Reclone or recreate the directory

		4) try vagrant up again

		5) Windows users - there could be a ssh timeout that could be caused from a firewall blocking the ssh connection (try turning off firewall software)

#Useful Commands
	$vagrant up -> start the vm

	$vagrant ssh -> ssh into the virtual machine (if in windows, easier to use virtualbox vm)

	$vagrant halt -> shuts down vm

	$vagrant destroy -> destroys vm, removes all vm files

	$devploy -> builds the website

	$launch -> starts servers (leave terminal open)

	$genprob -> erases current problems from database and regenerates the old and new problems


#Updating/Adding problems
If you update/add problems,

	$genprob

#Important
-After first time using 'vagrant up', you will have to 'vagrant ssh' into the system and run 'devploy' & 'launch'

-After the 'launch' command, the terminal being used will be unusable while running. If that terminal is closed, the servers are closed.

Built on pico platform2
