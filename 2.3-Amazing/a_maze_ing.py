#!/usr/bin/env python3
import sys
from typing import Any


class Config:
	def config_load(self) -> str:
		read_content = ""
		try:
			with open("config.txt", "r") as config_txt:
				read_content = config_txt.read()
				print(read_content)
		except FileNotFoundError:
			raise FileNotFoundError("FAILED TO FIND THE CONFIG FILE")
		return read_content
	
	def config_parse(self, context: str) -> dict[str, Any]:
		try:
			config_: dict[str, Any] = {}
			lines = context.split("\n")
			for line in lines:
				if line.strip():
					lvalue = line.split("=")[0]
					rvalue = line.split("=")[1]
					config_[lvalue] = rvalue
		except Exception:
			raise Exception("FAILED TO READ THE CONFIG FILE")
		return config_
	def config_validate(self, config_dict: dict[str, Any]) -> bool:
		try:
			if "WIDTH" not in config_dict or "HEIGHT" not in config_dict :
				raise Exception("MAZE SIZE NOT SPECIFIED IN CONFIG")
			if config_dict["WIDTH"] == "" or config_dict["HEIGHT"] == "":
				raise Exception("MAZE SIZE IS EMPTY IN CONFIG")
			if int(config_dict["WIDTH"]) <= 0  or int(config_dict["HEIGHT"]) <= 0:
				raise Exception("MAZE SIZE IS ZERO/ NEGATIVE IN CONFIG")
			if "start_point" not in config_dict:
				raise Exception("START POINT NOT SPECIFIED IN CONFIG")
			if "end_point" not in config_dict:
				raise Exception("END POINT NOT SPECIFIED IN CONFIG")
		except Exception as e:
			print(e)
			return False
		return True

class Maze:
    	pass


if __name__ == "__main__":
    print("=== A-Maze-ing ===")
    arg_len: int = len(sys.argv)

    if arg_len == 1:
        print("No arguments provided!")
    if arg_len == 1:
        print(f"Program name: {sys.argv[0]}")
        print(f"Arguments received: {arg_len - 1}")
        i: int = 1
        while i < arg_len:
            print(f"Argument {i}: {sys.argv[i]}")
            i += 1
    print(f"Total arguments: {arg_len}\n")

conf_obj = Config()
conf_txt = conf_obj.config_load()
config_dict = conf_obj.config_parse(conf_txt)
conf_obj.config_validate(config_dict)

print(config_dict)
