import java.util.*;

class DiningPhilosopher{
	public static void main(String[] args) 
	{
		Philosopher philosopher[] = new Philosopher[5];

		for(int id=0; id<5; id++){
			philosopher[id] = new Philosopher(id);
			philosopher[id].start();		
		}
	}
}


class Semaphores
{
	static int fork[] = {1,1,1,1,1};

	public static void sem_wait(int id)
	{
		while(fork[id]==0);
		fork[id]--;
	}

	public static void sem_signal(int id)
	{
		fork[id]++;
	}
}

class Philosopher extends Thread
{
	int id;
	public Philosopher(int id) {
		this.id = id;
	}

	public void run()
	{
		if(id != 4){
			System.out.println("Philosopher"+id+" is thinking");
			Semaphores.sem_wait(id);
			Semaphores.sem_wait((id+1)%5);			
			System.out.println("Philosopher"+id+" is eating");
			Semaphores.sem_signal((id+1)%5);	
			Semaphores.sem_signal(id);
			System.out.println("Philosopher"+id+" is releasing the fork");
		}
		else {
			System.out.println("Philosopher"+id+" is thinking");
			Semaphores.sem_wait((id+1)%5);
			Semaphores.sem_wait(id);			
			System.out.println("Philosopher"+id+" is eating");
			Semaphores.sem_signal(id);
			Semaphores.sem_signal((id+1)%5);	
			System.out.println("Philosopher"+id+" is releasing the fork");
		}	
	}
}
