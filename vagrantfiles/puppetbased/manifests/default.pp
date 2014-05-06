class pip {
	exec {"easy_install pip":
		path => "/usr/local/bin:/usr/bin:/bin",
		onlyif => "which easy_install",
		unless => "which pip",
	}
}

class devbox {
	package {["python", "python-devel", "python-setuptools", "vim-enhanced", "emacs", "elinks", "gcc", "gcc-c++", "java", "java-devel", "make", "git", "subversion"]:}

	class {"pip":}
}

node default {
	package {["vim-enhanced", "emacs", "elinks"]:}

	file {"/etc/motd":
		content => "Build using Vagrant and Puppet\n",
	}
}

node devbox {
	class {"devbox":}

	file {"/etc/motd":
		content => "This is a development machine made using Vagrant and Puppet\n",
	}
}
