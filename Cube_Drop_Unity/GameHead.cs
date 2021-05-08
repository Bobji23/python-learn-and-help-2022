using UnityEngine;
using UnityEngine.SceneManagement;

public class GameHead : MonoBehaviour {

	bool gameHasEnded = false;

	public float restartDelay = 1f;

	public GameObject completeLevelUI;
	
	public void CompleteLevel ()
	{
		Debug.Log("Level Won");
		
	}

	public void EndGame ()
	{
		if (gameHasEnded == false)
		{
			gameHasEnded = true;
			Debug.Log("GAME OVER");
			Invoke("Restart", restartDelay);
		}
	}

	void Restart ()
	{
		SceneManager.LoadScene("GameOver");
	}

}
