volatile boolean done1;
unsigned long start1;

float pwm1;
float pwmOld;
float pwmFiltered1;

unsigned long currentMicros;
unsigned long previousMicros;

int pot1;
int pot2;
int pot3;

float output1 = 0;
float output1Filtered = 0;

int flag = 0;

void setup() {
  pinMode(2, INPUT);
  pinMode(6, OUTPUT);
  pinMode(A0, INPUT);
  pinMode(A1, INPUT);
  pinMode(A2, INPUT);
  attachInterrupt(2, timeit, CHANGE); 
  }


void loop() {

      currentMicros = micros();

      pot1 = analogRead(A1);
      pot2 = analogRead(A0);
      pot3 = analogRead(A2);

      pot1 = map(pot1,0,1023,1,8);
      pot2 = map(pot2,0,1023,1,8);
      pot3 = map(pot3,0,1023,0,6000);


      if (flag == 0 && currentMicros - previousMicros >= (output1Filtered*pot1)) {
        digitalWrite(6, HIGH);
        previousMicros = currentMicros;
        flag = 1;
      }
      else if (flag == 1 && currentMicros - previousMicros >= (output1Filtered*(8-pot1)))  {
        digitalWrite(6, LOW);
        previousMicros = currentMicros;
        flag = 0;
      }   

      if (pwm1 < 30 ) {
        pwm1 = pwmOld;
      }
      pwmOld = pwm1; 
           
      output1 = (pwm1 * (pwm1*pot2))/1000;

      output1Filtered = filter(output1, output1Filtered, pot3);  

  }

void timeit() {
    if (digitalRead(2) == HIGH) {
      start1 = micros();
    }
    else {
      pwm1 = micros() - start1;
      done1 = true;
    }
  }


float filter(float prevValue, float currentValue, int filter) {  
  float lengthFiltered =  (prevValue + (currentValue * filter)) / (filter + 1);  
  return lengthFiltered;  
}









