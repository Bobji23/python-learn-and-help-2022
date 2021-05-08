using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class EndingGameYAY : MonoBehaviour
{
	public void Restart()
	{
		SceneManager.LoadScene("SampleScene");
	}
	public void Exit()
	{
		Debug.Log("IT WORKED");
     		Application.Quit();   
    	}
}



