#!/usr/bin/python
import whois
import dns
import dns.resolver


dom1 = str(raw_input("Introduce el primer objetivo: "))
dom2 = str(raw_input("Introduce el segundo objetivo: "))

print "---------------------------------------------------------------"

print "Primer Objetivo:"+ (dom1) 
print 
print "Informacion sobre los DNS de "+(dom1) 
print 
res = dns.resolver.query(dom1,'MX')

resns = dns.resolver.query(dom1,'NS')

resa = dns.resolver.query(dom1,'A')

resaaaa = dns.resolver.query(dom1,'AAAA')

ressoa = dns.resolver.query(dom1,'SOA')

restxt = dns.resolver.query(dom1,'TXT')


for rdata in res:
   print ('Host: ', rdata.exchange, 'has preference', rdata.preference)
for rdata in resns:
    print (rdata)

for rdata in resa:
    print (rdata)

for rdata in resaaaa:
    print (rdata)

for rdata in ressoa:
    print (rdata)

for rdata in restxt:
    print (rdata)
print 
print
print "WHOIS de "+ (dom1)
print 
print
host1 = dom1
resu = whois.whois(host1)
print resu

print "---------------------------------------------------------------"

print "Segundo Objetivo:"+ (dom2)
print
print "Informacion sobre los DNS de "+(dom2)
print 
res = dns.resolver.query(dom2,'MX')

resns = dns.resolver.query(dom2,'NS')

resa = dns.resolver.query(dom2,'A')

resaaaa = dns.resolver.query(dom2,'AAAA')

ressoa = dns.resolver.query(dom2,'SOA')

restxt = dns.resolver.query(dom2,'TXT')

for rdata in res:
   print ('Host: ', rdata.exchange, 'has preference', rdata.preference)
for rdata in resns:
    print (rdata)

for rdata in resa:
    print (rdata)

for rdata in resaaaa:
    print (rdata)

for rdata in ressoa:
    print (rdata)

for rdata in restxt:
    print (rdata)

print
print
print "WHOIS de "+(dom2)
print
print
host2 = dom2
resu = whois.whois(host2)
print resu

