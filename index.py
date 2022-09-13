// C++ code
int  contador=0; 
int subeBaja;
int i;
void setup()
{
  
  #define E 2
  #define D 3
  #define C 4
  #define G 6
  #define H 5
  #define F 7
  #define A 8
  #define B 9
  #define TOGGLE A0
  pinMode(13, OUTPUT);
  pinMode(E, OUTPUT);
  pinMode(D, OUTPUT);
  pinMode(C, OUTPUT);
  pinMode(H, OUTPUT);
  pinMode(G, OUTPUT);
  pinMode(F, OUTPUT);
  pinMode(A, OUTPUT);
  pinMode(B, OUTPUT);
  pinMode(TOGGLE, INPUT_PULLUP);
}

void loop()
{

  
  
  
  if(digitalRead(A0)==(0)){

   relojNumeros(contador);
   delay(1500); 
    apagar();
    contador++;
  
    
  
  }else
  {
   relojNumeros(contador);
   delay(1500);
   apagar();
   contador--;
  }
	
  	
 
    if (contador==(-1)){
        contador=3;
    }
     if (contador==(4)){
        contador=-1;
    }
 
}
void apagar(void){
        digitalWrite(E, LOW);
        digitalWrite(D, LOW);
        digitalWrite(C, LOW);
        digitalWrite(F, LOW);
        digitalWrite(A, LOW);
        digitalWrite(B, LOW);
        digitalWrite(G, LOW);
        digitalWrite(H, LOW);
  		digitalWrite(13, LOW);
}

void relojNumeros(int numero){

switch(numero){
  case 4:
        digitalWrite(A, HIGH);
        digitalWrite(B, HIGH);
        digitalWrite(C, HIGH);
        digitalWrite(D, HIGH);
        digitalWrite(E, HIGH);
  		digitalWrite(F, HIGH);
          break; 
  
    case 3:
        digitalWrite(A, HIGH);
        digitalWrite(B, HIGH);
        digitalWrite(C, HIGH);
        digitalWrite(D, HIGH);
        digitalWrite(E, HIGH);
  		digitalWrite(F, HIGH);
 		 digitalWrite(13, HIGH);
          break;
    case 2:
        digitalWrite(E, HIGH);
        digitalWrite(C, HIGH);
        digitalWrite(G, HIGH);
   		digitalWrite(13, HIGH);

          break;
    case 1:
        digitalWrite(D, HIGH);
    	digitalWrite(13, HIGH);
          break;
    case 0:
        digitalWrite(H, HIGH);
        
	  break;
	}

}