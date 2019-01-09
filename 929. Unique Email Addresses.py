"""
Every email consists of a local name and a domain name, separated by the @ sign.

For example, in alice@leetcode.com, alice is the local name, and leetcode.com is the domain name.

Besides lowercase letters, these emails may contain '.'s or '+'s.

If you add periods ('.') between some characters in the local name part of an email address, mail sent there will be forwarded to the same address without dots in the local name.  For example, "alice.z@leetcode.com" and "alicez@leetcode.com" forward to the same email address.  (Note that this rule does not apply for domain names.)

If you add a plus ('+') in the local name, everything after the first plus sign will be ignored. This allows certain emails to be filtered, for example m.y+name@email.com will be forwarded to my@email.com.  (Again, this rule does not apply for domain names.)

It is possible to use both of these rules at the same time.

Given a list of emails, we send one email to each address in the list.  How many different addresses actually receive mails?



Example 1:

Input: ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
Output: 2
Explanation: "testemail@leetcode.com" and "testemail@lee.tcode.com" actually receive mails
"""

emails=["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
# My solution
# Output = []
# for email in emails:
#     email_split = email.split('@')
#     local_name = email_split[0]
#     domain_name = email_split[1]
#     if '+' in local_name:
#         local_name_split = local_name.split('+')
#         local_name = list(local_name_split[0])
#         while True:
#             if '.' not in local_name:
#                 break
#             local_name.remove('.')
#     local_name = "".join(str(l) for l in local_name)
#     Output.append(local_name + '@' + domain_name)

# Amazing solution
email_set=set()
for email in emails:
    local_name,domain_name = email.split('@')
    local_name=''.join(local_name.split('+')[0].split('.'))
    email=local_name + '@' + domain_name
    email_set.add(email)