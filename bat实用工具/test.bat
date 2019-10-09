@echo off
title 测试脚本
echo 当前CMD工作目录：%cd%
echo 当前bat 文件所在盘符：%~d0 
echo 当前bat 文件所在目录：%~dp0
echo 当前bat 文件短文路径：%~sdp0
echo 当前bat 文件完整路径：%~f0
 
cd %~d0
echo cd到当前bat 文件所在盘符后，CMD默认目录：%cd%
 
cd %~dp0
echo cd到当前bat 文件所在目录后，CMD默认目录：%cd%
 
pause