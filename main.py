from raylib import *

InitWindow(420,560,"2048".encode("utf-8"))
SetTargetFPS(60)

while not WindowShouldClose():
    BeginDrawing()
    ClearBackground((250,248,239))
    EndDrawing()

CloseWindow()