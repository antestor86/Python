import subprocess

"""Test"""
path = r"C:/Users/razmik.avetisyan/Desktop/log.txt"

out = open(path,'a')

proc = subprocess

proc.call(['ping','-t','QS0301601'],stdout=out)