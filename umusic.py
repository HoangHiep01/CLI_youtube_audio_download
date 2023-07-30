import argparse
from pytube import YouTube
import os



def main(link=None, folder=None):

	if link == None:
		print("YouTube's link required")

	try:
		out_path = os.getcwd() + "\\" + "Downloads\\Music\\"
		if folder is not None:
			out_path += folder
		
		yt = YouTube(link)
		audio_list = yt.streams.filter(only_audio=True)

		print(f"Choose options: (from 0 to {len(audio_list)-1})")
		for idx, opt in enumerate(audio_list):
			print(idx, opt)

		idx = int(input("Your option is: "))
		print(f"Your choose is {audio_list[idx]}")
		audio_option = audio_list[idx]
		
		out_file = audio_option.download(output_path=out_path)


		base, ext = os.path.splitext(out_file)
		new_file = base + '.mp3'
		os.rename(out_file, new_file)

	except Exception as e:
		print("Error - " + str(e))

	else:
		print("Save's path: " + out_path)
		print(yt.title + " has been successfully downloaded.")

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='Download audio from Youtube.')
	parser.add_argument('--link', metavar="link", type=str, default=None, required=True, action="store", help='Link video on YouTube that you want download the audio.')
	parser.add_argument('--folder', metavar="folder", type=str, default=None, action="store", help='Save path. None for current folder. If give folder link is current folder + link.')
	args = parser.parse_args()
	main(args.link, args.folder)
