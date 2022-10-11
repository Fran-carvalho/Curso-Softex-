
//Serialização

//1 - Crie um objeto FileOutputStream

 FileOutputStream fileStream = new FileOutputStream("MyGame.teste");

 //2 - Crie um ObjectOutputStream

 ObjectOutputStream os = new ObjectOutputStream(fileStream);

 //3 - Grave os objetos

 os.writeObject(personagemUm); //Serializa os objetos referenciados por
 os.writeObject(personagemDois);//personagemUm,personagemDois,personagemTres
 os.writeObject(personagemTres); //e grava no arquivo myGame.ser

 //4 - Feche ObjectOutputStream
 os.close;

 //Desserialização

 //1 - Crie um objeto FileInputStream
 FileInputStream fileStream = new FileInputStream("MyGame.teste");

 //2 - Crie um ObjectInputStream

 ObjectInputStream os = new ObjectInputStream(fileStream);

 //3 - Leia os objetos

 Object um = os.readObject();
 Object dois = os.readObject();
 Object tres = os.readObject();

 //4 - Converta os objetos

 GamePersonagem elfo   = (GamePersonagem) um;
 GamePersonagem rei = (GamePersonagem) dois;
 GamePersonagem bruxo   = (GamePersonagem) tres;

 //5 - Feche ObjectInputStream

 os.close();
