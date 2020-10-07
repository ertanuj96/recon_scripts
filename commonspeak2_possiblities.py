import sys


# pass the domain name as argument to script
scope_ = sys.argv[1:]
scope = scope_[0]
wordlist1 = open('/home/ec2-user/tools/commonspeak2-wordlists/subdomains/subdomains.txt').read().split('\n')

for word in wordlist1:
    if not word.strip(): 
        continue
    print('{}.{}'.format(word.strip(), scope))

wordlist2 = open('/home/ec2-user/tools/SecLists/Discovery/DNS/clean-jhaddix-dns.txt').read().split('\n')

for word in wordlist2:
    if not word.strip():
        continue
    print('{}.{}'.format(word.strip(), scope))

wordlist3 = open('/home/ec2-user/tools/SecLists/Discovery/DNS/subdomains-top1million-110000.txt').read().split('\n')

for word in wordlist3:
    if not word.strip():
        continue
    print('{}.{}'.format(word.strip(), scope))

