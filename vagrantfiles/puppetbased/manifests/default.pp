class pip {
	package {"python-setuptools":}

	exec {"easy_install pip":
		path => "/usr/local/bin:/usr/bin:/bin",
		onlyif => "which easy_install",
		unless => "which pip",
		require => Package["python-setuptools"],
	} -> file {"pip-link":
		target => "/usr/bin/pip",
		ensure => "link",
		path => "/usr/bin/pip-python",
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

node ipython {
	class {"pip":}

	package {["python", "python-devel", "python-matplotlib", "python-gtkextra", "vim-enhanced", "emacs", "elinks", "gcc", "gcc-c++", "make", "git", "subversion", "blas-devel", "lapack-devel", "freetype-devel"]:}

	file {"/etc/motd":
		content => "This is an ipython notebook server made using Vagrant and Puppet\n"
	}

	package {["pygments", "tornado", "jinja2", "Cython"]:
		provider => "pip",
		require => Class["pip"],
	}
	package {"numpy >= 1.8.1":
		provider => "pip",	
		require => [Class["pip"], Package["blas-devel"], Package["lapack-devel"]],
	}
	package {"scipy":
		provider => "pip",
		require => Package["numpy >= 1.8.1"],
	}

	github::clone {"ipython":
		projectname => "ipython/ipython",
	}

	github::checkout {"ipython rel-1.2.1":
		project => "ipython",
		branch => "rel-1.2.1",
		require => Github::Clone["ipython"], 
	}

	github::install {"ipython":
		project => "ipython",
		require => Github::Checkout["ipython rel-1.2.1"],
		unless => "which ipython",
	}

	github::clone {"zeromq/pyzmq":
		projectname => "zeromq/pyzmq",
		require => Package["Cython"],
	} ->
	github::install {"zeromq/pyzmq":
		project => "pyzmq",
		unless => "pip freeze |grep zmq",
		require => Class["pip"],
	}

}
