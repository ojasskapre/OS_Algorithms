import java.util.Scanner;
import java.util.Vector;

class BinarySemaphore {
	public static void main(String[] args) {
		int buf_size;
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter capacity: ");
		buf_size = sc.nextInt();
		Container con = new Container(buf_size);
		Producer p1 = new Producer(con, 1);
		Producer p2 = new Producer(con, 2);
		Producer p3 = new Producer(con, 3);
		Consumer c = new Consumer(con);
		p1.start();
		p2.start();
		p3.start();
		c.start();
	}
}


class Semaphores {
	static boolean flag = true;
	
	public static void s_wait() {
		while(!flag);
		flag = false;
	}
	
	public static void s_signal() {
		flag = true;
	}
}

class Container{
	int buf_size, total_products;
	Vector container;
	
	public Container(int buf_size){
		this.buf_size = buf_size;
		container = new Vector(buf_size);
		total_products = 0;
	}
	
	public void inserts(int pid,int id){
		if(buf_size != total_products){
			System.out.println("Producer"+id+" produces "+pid);
			container.add(pid);
			total_products++;
		}
		else{
			System.out.println("Conatiner Full....Unable to add");
		}
	}
	
	public void deletes(){
		if(total_products != 0){
			System.out.println("Consumer consumes "+container.get(0));
			container.removeElementAt(0);
			total_products--;
		}
		else {
			System.out.println("Conatiner Empty....Nothing to consume");
		}
	}
}

class Producer extends Thread{
	Container con;
	int id;
	public Producer(Container con, int id){
		this.con = con;
		this.id = id;
	}
	
	public void run(){
		int i;
		for(i=0; i<10; i++){
			Semaphores.s_wait();
			con.inserts(i,id);
			Semaphores.s_signal();
		}
	}
}

class Consumer extends Thread{
	Container con;
	
	public Consumer(Container con){
		this.con = con;
	}

	public void run(){
		int i;
		for(i=0; i<10; i++){
			Semaphores.s_wait();
			con.deletes();
			Semaphores.s_signal();
		}
	}
}
