try:
    import os,re,subprocess;from colorama import Fore;from requests import get,post;from time import sleep;from rich.console import Console
    console=Console();console.print()
except Exception as e:print(f'[!] Download The Missing Module ! , {e}');exit()

#Beta for Linux Only
 
def Wifi_Hotspot(usewlan):
    usewlan0=usewlan+'mon';usewlan1=usewlan
    console.log(f"[!] Warning: After You Done use This Commmand in Terminal ( sudo airmon-ng stop {usewlan0}mon or {usewlan0} ) or ( sudo airmon-ng stop {usewlan1} or {usewlan1}mon )!");sleep(0.9)
    Fake_hotspotmaker=subprocess.run(["sudo","mdk3",usewlan0,"b","-c","1","-f","SSID.lst"],capture_output=True,text=True).stdout
    if "<class 'str'>" in str(type(Fake_hotspotmaker)):
        Fake_hotspotmaker=subprocess.run(["sudo","mdk3",usewlan1,"b","-c","1","-f","SSID.lst"],capture_output=True,text=True).stdout
        if "<class 'str'>" in str(type(Fake_hotspotmaker)):console.log('[!] Error . ');exit()
    #console.log(Fake_hotspotmaker)

def config():           
    input(f"[{Fore.LIGHTRED_EX}!{Fore.RESET}] {Fore.RED}Before You Start, Exit Your Wifi, if You Done Press Enter .{Fore.RESET}");print('\n');loads=[f"{n}" for n in range(1,11)]
    ifconfig=subprocess.run(["ifconfig"],capture_output=True,text=True).stdout
    for wlan in re.findall('wlan(.*?):',ifconfig):console.log(f'[{wlan[0]}] WLAN ')
    wl=input(f'\n[{Fore.LIGHTRED_EX}?{Fore.RESET}] The interface you will use : ');usewlan='wlan'+wl;print('\n')
    if wl not in wlan:console.log('[!] You must choose wlan you have only !');exit()
    try:air=subprocess.run(["sudo","airmon-ng","start",usewlan],capture_output=True,text=True).stdout
    except Exception as e:console.log(f'[!] Error Found >> {e}');exit()
    if 'monitor mode enabled' in air:
        console.log("[+] Trying To Enable Monitor Mode ..");sleep(2);console.log("[+] Monitor Mode Enabled ");sleep(1)
        with console.status("[bold green]Loading ...") as status:
            while loads:load=loads.pop(0);sleep(1)
        console.log("[+] Trying To Crate Fake HotSpots ..");sleep(2);console.log("[+] Successfully Created Fake HotSpots .");sleep(2);Wifi_Hotspot(usewlan)
    elif 'monitor mode already enabled for' in air:
        console.log("[+] Trying To Enable Monitor Mode ..");sleep(1);console.log("[+] Monitor Mode Enabled ");sleep(1)
        Ender=subprocess.run(["sudo","airmon-ng","stop",usewlan],capture_output=True,text=True).stdout
        if 'monitor mode disabled' in Ender:
            try:air=subprocess.run(["sudo","airmon-ng","start",usewlan],capture_output=True,text=True).stdout
            except Exception as e:console.log(f'[!] Error Found >> {e}');exit()
            with console.status("[bold green]Loading ...") as status:
                while loads:load=loads.pop(0);sleep(1)
            console.log("[+] Trying To Crate Fake HotSpots ..");sleep(1);console.log("[+] Successfully Created Fake HotSpots .");sleep(2);Wifi_Hotspot(usewlan)
        elif 'You are trying to stop' in Ender:
            try:air=subprocess.run(["sudo","airmon-ng","start",usewlan],capture_output=True,text=True).stdout
            except Exception as e:console.log(f'[!] Error Found >> {e}');exit()
            with console.status("[bold green]Loading ...") as status:
                while loads:load=loads.pop(0);sleep(1)
            console.log("[+] Trying To Crate Fake HotSpots ..");sleep(1);console.log("[+] Successfully Created Fake HotSpots .");sleep(2);Wifi_Hotspot(usewlan)
        else:console.log("[!] Can't Shutdown Monitor Mode You Must Do it Manually With : ( sudo airmon-ng stop wlan1 )");sleep(1)
    elif 'monitor mode vif enabled' in air:
        console.log("[+] Trying To Enable Monitor Mode ..");sleep(1);console.log("[+] Monitor Mode Enabled ");sleep(1)
        with console.status("[bold green]Loading ...") as status:
            while loads:load=loads.pop(0);sleep(1)
        console.log("[+] Trying To Crate Fake HotSpots ..");sleep(1);console.log("[+] Successfully Created Fake HotSpots .");sleep(2);Wifi_Hotspot(usewlan)
    else:
        try:
            Ender=subprocess.run(["sudo","airmon-ng","stop",usewlan+'mon'],capture_output=True,text=True).stdout
            if 'monitor mode vif disabled' in Ender:
                try:air=subprocess.run(["sudo","airmon-ng","start",usewlan],capture_output=True,text=True).stdout
                except Exception as e:console.log(f'[!] Error Found >> {e}');exit()
                console.log("[+] Trying To Enable Monitor Mode ..");sleep(1);console.log("[+] Monitor Mode Enabled ");sleep(1)
                with console.status("[bold green]Loading...") as status:
                    while loads:load=loads.pop(0);sleep(1)
                console.log("[+] Trying To Crate Fake HotSpots ..");sleep(1);console.log("[+] Successfully Created Fake HotSpots .");sleep(2);Wifi_Hotspot(usewlan)
        except:pass
        sleep(1);console.log("[!] Failed Enable Monitor Mode ..");exit()

def Header():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""
███████╗ █████╗ ██╗  ██╗███████╗    ██╗    ██╗██╗███████╗██╗
██╔════╝██╔══██╗██║ ██╔╝██╔════╝    ██║    ██║██║██╔════╝██║
█████╗  ███████║█████╔╝ █████╗█████╗██║ █╗ ██║██║█████╗  ██║
██╔══╝  ██╔══██║██╔═██╗ ██╔══╝╚════╝██║███╗██║██║██╔══╝  ██║
██║     ██║  ██║██║  ██╗███████╗    ╚███╔███╔╝██║██║     ██║
╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝     ╚══╝╚══╝ ╚═╝╚═╝     ╚═╝

              By @TweakPY - @vv1ck
""") 
    console.log('[-] Started Fake-Wifi ...\n')
    config()
Header()
