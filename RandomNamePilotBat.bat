@echo off

rem 「for」コマンドを使った一定回数のループ (1, 1, N)のNに個数を入力する
for /l %%n in (1,1,5) do (
 
  rem RandomNamePilot
  echo RandomNamePilot
  call RandomNamePilot.exe
 
)