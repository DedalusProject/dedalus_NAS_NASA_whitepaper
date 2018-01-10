import mailbox
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('modern')

fname_users = "dedalus-users.mbox"
fname_dev = "dedalus-dev.mbox"

users = mailbox.mbox(fname_users)
dev = mailbox.mbox(fname_dev)
mailboxes = {'users':users, 'dev':dev}
s = {}
for k,mb in mailboxes.items():
    dates = []
    email = []

    for m in mb:
        dates.append(pd.to_datetime(m['date']))
        email.append(m['from'])

    s[k] = pd.Series(email,index=dates)

print("users: {:d} unique email addresses.".format(len(s['users'].unique())))
print("dev: {:d} unique email addresses.".format(len(s['dev'].unique())))

# bin into months, get message counts
message_counts = {}
for k in s.keys():
    message_counts[k] = s[k].resample('M').count()

fig = plt.figure()
p = message_counts['users'][:-1].plot(label='dedalus-users') # trim off Jan 2018
p = message_counts['dev'][:-1].plot(label='dedalus-dev') # trim off Jan 2018
p.set_ylim(0,100)
p.set_ylabel('Messages to dedalus lists')
p.legend(loc='upper left').draw_frame(False)
fig.savefig('../figs/message_counts.png',dpi=300)
