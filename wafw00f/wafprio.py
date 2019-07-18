#!/usr/bin/env python
'''
Copyright (C) 2019, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

# NOTE: this priority list is used so that each check can be prioritized,
# so that the quick checks are done first and ones that require more
# requests, are done later


wafdetectionsprio = [
    # cached default request ones first
    'Yunjiasu (Baidu Cloud Computing)',
    'PowerCDN (PowerCDN)',
    'ChinaCache CDN Load Balancer (ChinaCache)',
    'Edgecast (Verizon Digital Media)',
    'Profense (ArmorLogic)',
    'West263 Content Delivery Network',
    'NevisProxy (AdNovum)',
    'NetContinuum (Barracuda Networks)',
    'Cloudflare (Cloudflare Inc.)',
    'NSFocus (NSFocus Global Inc.)',
    'DOSarrest (DOSarrest Internet Security)',
    'Comodo cWatch (Comodo CyberSecurity)',
    'Wallarm (Wallarm Inc.)',
    'BlockDoS (BlockDoS)',
    'Mission Control Application Shield (Mission Control)',
    'Secure Entry (United Security Providers)',
    'ACE XML Gateway (Cisco)',
    'HyperGuard (Art of Defense)',
    'BinarySec (BinarySec)',
    'Teros (Citrix Systems)',
    'TransIP Web Firewall (TransIP)',
    'BIG-IP Access Policy Manager (F5 Networks)',
    'FirePass (F5 Networks)',
    'BIG-IP Local Traffic Manager (F5 Networks)',
    'Trafficshield (F5 Networks)',
    'DataPower (IBM)',
    # the next ones require attack strings to be sent
    'XLabs Security WAF (XLabs)',
    'Kona Site Defender (Akamai)',
    'aeSecure (aeSecure)',
    'Airlock (Phion/Ergon)',
    'Alert Logic (Alert Logic)',
    'AliYunDun (Alibaba Cloud Computing)',
    'Anquanbao (Anquanbao)',
    'AnYu (AnYu Technologies)',
    'Approach (Approach)',
    'Armor Defense (Armor)',
    'ASP.NET Generic Protection (Microsoft)',
    'Astra Web Protection (Czar Securities)',
    'Barikode (Ethic Ninja)',
    'Barracuda Application Firewall (Barracuda Networks)',
    'Bekchy (Faydata Technologies Inc.)',
    'BitNinja (BitNinja)',
    'Bluedon (Bluedon IST)',
    'CacheWall (Varnish)',
    'CdnNS Application Gateway (CdnNs/WdidcNet)',
    'WP Cerber Security (Cerber Tech)',
    'Chuang Yu Shield (Yunaq)',
    'Cloudbric (Penta Security)',
    'Cloudfront (Amazon)',
    'CrawlProtect (Jean-Denis Brun)',
    'DenyALL (Rohde & Schwarz CyberSecurity)',
    'Distil (Distil Networks)',
    'DotDefender (Applicure Technologies)',
    'DynamicWeb Injection Check (DynamicWeb)',
    'Expression Engine (EllisLab)',
    'BIG-IP Application Security Manager (F5 Networks)',
    'FortiWeb (Fortinet)',
    'GoDaddy Website Protection (GoDaddy)',
    'Greywizard (Grey Wizard)',
    'Imunify360 (CloudLinux)',
    'Incapsula (Imperva Inc.)',
    'Instart DX (Instart Logic)',
    'ISA Server (Microsoft)',
    'Janusec Application Gateway (Janusec)',
    'Jiasule (Jiasule)',
    'KS-WAF (KnownSec)',
    'LiteSpeed Firewall (LiteSpeed Technologies)',
    'Open-Resty Lua Nginx WAF',
    'Malcare (Inactiv)',
    'ModSecurity (SpiderLabs)',
    'NAXSI (NBS Systems)',
    'Nemesida (PentestIt)',
    'NetScaler AppFirewall (Citrix Systems)',
    'Newdefend (NewDefend)',
    'NexusGuard Firewall (NexusGuard)',
    'NinjaFirewall (NinTechNet)',
    'OnMessage Shield (BlackBaud)',
    'Palo Alto Next Gen Firewall (Palo Alto Networks)',
    'PerimeterX (PerimeterX)',
    'pkSecurity Intrusion Detection System',
    'AppWall (Radware)',
    'Reblaze (Reblaze)',
    'RSFirewall (RSJoomla!)',
    'ASP.NET RequestValidationMode (Microsoft)',
    'Safe3 Web Firewall (Safe3)',
    'Safedog (SafeDog)',
    'Safeline (Chaitin Tech.)',
    'eEye SecureIIS (BeyondTrust)',
    'SecuPress WordPress Security (SecuPress)',
    'SecureSphere (Imperva Inc.)',
    'SEnginx (Neusoft)',
    'Shield Security (One Dollar Plugin)',
    'SiteGround (SiteGround)',
    'SiteGuard (Sakura Inc.)',
    'Sitelock (TrueShield)',
    'SonicWall (Dell)',
    'UTM Web Protection (Sophos)',
    'Squarespace (Squarespace)',
    'StackPath (StackPath)',
    'Sucuri CloudProxy (Sucuri Inc.)',
    'Tencent Cloud Firewall (Tencent Technologies)',
    'URLMaster SecurityCheck (iFinity/DotNetNuke)',
    'URLScan (Microsoft)',
    'Varnish (OWASP)',
    'VirusDie (VirusDie LLC)',
    'WatchGuard (WatchGuard Technologies)',
    'WebARX (WebARX Security Solutions)',
    'WebKnight (AQTRONIX)',
    'WebSEAL (IBM)',
    'WebTotem (WebTotem)',
    'Wordfence (Feedjit)',
    'WTS-WAF (WTS)',
    '360WangZhanBao (360 Technologies)',
    'Xuanwudun',
    'Yundun (Yundun)',
    'Yunsuo (Yunsuo)',
    'Zenedge (Zenedge)',
    'ZScaler (Accenture)'
]
