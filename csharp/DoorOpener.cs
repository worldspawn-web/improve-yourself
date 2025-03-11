using UnityEngine;

public class DoorOpener : MonoBehaviour
{
    private Animator doorAnimator;

    void Start()
    {
        doorAnimator = GetComponent<Animator>();
    }

    private void OnTriggerEnter(Collider other)
    {
       // Check if the object entering the trigger is player
       if (other.CompareTag("Player"))
        {
            if (doorAnimator != null)
            {
                doorAnimator.SetTrigger("Door_Open");
            }
        }
    }

    void Update()
    {
        
    }
}
