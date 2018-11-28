# grow.it

This is a project to produce an open source growing system that is easy to use, set up and expand without needing expensive modules.

##Current Radio communication plan
-Channel always 32
    -Address reflective of role
        -Last bit addresses indicate slaves
        -[:-2] bit address indicate feedback
        -[:-3] bit address indicates master unit
    -grouping
        -group 2 for slaves
        -group 0 for controller
        -group 1 for actors/feedback controllers


##Light detection:
	This element of the system is still being developed and requires more work before being rolled out. The function detectLight() will be an independently threaded application, which should monitor light levels for one [1] hour and then send a list of light levels measured every 60s to the master controller. The remainder of processing numbers, averaging and acting on the data will be done on the master controller.

This multithreading can be achieved by downloading and installing async module "https://github.com/peterhinch/micropython-async/blob/master/TUTORIAL.md#01-installing-uasyncio-on-bare-metal"

