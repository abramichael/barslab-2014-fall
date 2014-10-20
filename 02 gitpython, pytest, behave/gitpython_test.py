from git import *

#repo path
repo = Repo("F:\\praxis\\abr")

#print repo.untracked_files

#cloned_repo = repo.clone("F:\\praxis\\abr2")
#new_repo = repo.init("F:\\praxis\\abr3")

heads2 = repo.heads
master = heads2.master
master.rename("master2")
print master.commit


head2 = repo.head
master = head2.reference
#git log
log = master.log()
for item in log:
    print item

hc = repo.head.commit
#root dir of rep
hct = hc.tree

#trees - subdirs in folder
#blobs - list of files in folder
print hct.trees[0].path
print hct.blobs[0].data_stream.read()
print hct.blobs[1].data_stream.read()