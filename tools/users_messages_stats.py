import mailbox
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('modern')

fname = "dedalus-users.mbox"

dates = []
email = []

mb = mailbox.mbox(fname)
for m in mb:
    dates.append(pd.to_datetime(m['date']))
    email.append(m['from'])

s = pd.Series(email,index=dates)

# bin into months, get message counts
message_counts = s.resample('M').count()
print("{:d} unique email addresses.".format(len(s.unique())))

fig = plt.figure()
p = message_counts[:-1].plot() # trim off Jan 2018
p.set_ylabel('Messages to dedalus-users')
fig.savefig('message_counts.png',dpi=300)
