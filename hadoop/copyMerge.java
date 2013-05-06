import org.apache.hadoop.fs.FileUtil;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import java.net.URI;
import org.apache.hadoop.conf.Configuration;
import java.net.URISyntaxException;
import java.io.IOException;

public class copyMerge
{

    public static void print_usage()
    {
	System.out.println("Usage: copyMerge <input directory> <output file name>");
    }

    public static void main(String[] args)
    {
	Configuration conf = new Configuration();
	
	if(args.length != 2)
	    {
		System.err.println("Invalid number of arguments.");
		System.out.println("");
		print_usage();
		System.exit(1);
	    }

	String indir = args[0];
	String outfile = args[1];
	Path inpath = new Path(indir);
	Path outpath = new Path(outfile);
	FileSystem infs,outfs;
	infs = outfs = null;
	String addString = null;
	
	try
	    {
		infs = FileSystem.get(new URI(indir), conf);
		outfs = FileSystem.get(new URI(outfile), conf);
	    }
	catch(URISyntaxException urise)
	    {
		System.err.println("Could not load URI: " + urise.getInput());
		System.err.println("Reason: " + urise.getReason());
		System.exit(1);
	    }
	catch(IOException ioe)
	    {
		System.err.println("Could not get FileSystem: " + ioe.getMessage());
		System.exit(1);
	    }
	
	System.out.println("Merging " + indir + " into " + outfile);
	
	try
	    {
		boolean copySuccess = FileUtil.copyMerge(infs, inpath, outfs, outpath, false, conf, addString);
		if(copySuccess)
		    System.out.println("Copy succeeded.");
		else
		    System.out.println("Copy failed.");
	    }
	catch(IOException ioe)
	    {
		System.err.println("File merge failed: " + ioe.getMessage());
                System.exit(1);
	    }

    }

}