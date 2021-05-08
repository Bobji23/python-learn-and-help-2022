using UnityEngine;
using UnityEngine.SceneManagement;

public class EndTrigger : MonoBehaviour
{
	
	public GameHead gameHead;	

	void OnTriggerEnter ()
	{
		SceneManager.LoadScene("LevelComplete");
		
	}
}