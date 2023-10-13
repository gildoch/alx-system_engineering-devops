0. **0-iam_betty**
Script that switches the current user to the user betty.
---
1. **1-who_am_i**
Script that prints the effective username of the current user.
---
2. **2-groups**
Script that prints all the groups the current user is part of.
---
3. **3-new_owner**
Script that changes the owner of the file hello to the user betty.
---
4. **4-empty**
Script that creates an empty file called hello
---
5. **5-execute**
Script that adds execute permission to the owner of the file hello.
---
6. **6-multiple_permissions**
Script that adds execute permission to the owner and the group owner, and read permission to other users, to the file hello.
---
7. **7-everybody**
Script that adds execution permission to the owner, the group owner and the other users, to the file hello
---
8. **8-James_Bond**
Script that sets the permission to the file hello as follows:
- Owner: no permission at all
- Group: no permission at all
- Other users: all the permissions
---
9. **9-John_Doe**
script that sets the mode of the file hello to this: -rwxr-x-wx 1 julien julien 23 Sep 20 14:25 hello
---
10. **10-mirror_permissions**
Script that sets the mode of the file hello the same as olleh’s mode.
Note: the mode of olleh will not always be 664. Make sure your script works for any mode.
---
11. **11-directories_permissions**
Script that adds execute permission to all subdirectories of the current directory for the owner, the group owner and all other users. Regular files should not be changed.
---
12. **12-directory_permissions**
Script that creates a directory called my_dir with permissions 751 in the working directory.
---
13. **13-change_group**
Script that changes the group owner to school for the file hello 
---
14. **100-change_owner_and_group**
Script that changes the owner to vincent and the group owner to staff for all the files and directories in the working directory.
---
15. **101-symbolic_link_permissions***
Script that changes the owner and the group owner of _hello to vincent and staff respectively.
---
16. **102-if_only**
Script that changes the owner of the file hello to betty only if it is owned by the user guillaume.
---
17. **103-Star_Wars**
Script that will play the StarWars IV episode in the terminal.
