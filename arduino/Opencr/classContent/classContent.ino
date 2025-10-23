
#include "songs.h"
#include "sensors.h"

int criticalnote = NOTE_A4;
float criticalVoltage = 11.5;
unsigned long lastBatteryCheck = 0; 

void setup() {
  Serial.begin(115200);
  Serial.println("Launching IMU");
  IMU.begin();
  Serial.println("Playing start melody");
  playSequence(DarthVader, noteDurations_DarthVader);
  pinMode(led_pin, OUTPUT);
}

float checkCriticalBattery() {
  float voltage = getBatteryVoltage();
  Serial.println("battery check");

  while (voltage < criticalVoltage) {
    tone(BDPIN_BUZZER, NOTE_A4, 100);
    Serial.println("Battery critical ");
    float voltage = getBatteryVoltage();
    delay(1000);

  }

  return false;
}

void loop() {

  float roll = getRoll();
  float yaw = getYaw();
  float pitch = getPitch();

  bool criticalVoltageBool = false;
  float voltage = getBatteryVoltage();

  if(millis() - lastBatteryCheck >= 60000 )
  {

    lastBatteryCheck = millis();
    criticalVoltageBool = checkCriticalBattery();

  }


  Serial.print("Battery voltage: ");
  Serial.print(voltage);
  Serial.print(" ,Roll: ");
  Serial.print(roll);
  Serial.print(",Pitch: ");
  Serial.print(pitch);
  Serial.print(" ,Yaw: ");
  Serial.println(yaw);
  delay(100);
}