# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .forms import *
from .models import *
#from context.models import *
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from django.template import RequestContext
from django import forms
from django.forms import modelformset_factory






# -------------------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------- #
#
#                                            Create your views here  
#
# -------------------------------------------------------------------------------------------------- #
@login_required
def alias(request, pk_bundle):
    print ' \n\n \n\n-------------------------------------------------------------------------'
    print '\n\n---------------------- Add an Alias with ELSA ---------------------------'
    print '------------------------------ DEBUGGER ---------------------------------'

    # Get Bundle
    bundle = Bundle.objects.get(pk=pk_bundle)
#    collections = Collections.objects.get(bundle=bundle)

    # Secure ELSA by seeing if the user logged in is the same user associated with the Bundle
    if request.user == bundle.user:
        print 'authorized user: {}'.format(request.user)

        # ELSA's current user is the bundle user so begin view logic
        # Get forms
        form_alias = AliasForm(request.POST or None)

        # Declare context_dict for templating language used in ELSAs templates
        context_dict = {
            'form_alias':form_alias,
            'bundle':bundle,

        }

        # After ELSAs friend hits submit, if the forms are completed correctly, we should enter
        # this conditional.
        print '\n\n------------------------------- ALIAS INFO --------------------------------'
        print '\nCurrently awaiting user input...\n\n'
        if form_alias.is_valid():
            print 'form_alias is valid for {}.'.format(bundle.user)
            # Create Alias model object
            alias = form_alias.save(commit=False)
            alias.bundle = bundle
            alias.save()
            print 'Alias model object: {}'.format(alias)

            # Find appropriate label(s).
            # Alias gets added to all Product_Bundle & Product_Collection labels.
            # We first get all labels of these given types except those in the Data collection which
            # are handled different from the other collections.
            all_labels = []
            product_bundle = Product_Bundle.objects.get(bundle=bundle)
            product_collections_list = Product_Collection.objects.filter(bundle=bundle).exclude(collection='Data')
            # We need to check for Product_Collections associated with Data products now.
                    
            all_labels.append(product_bundle)
            all_labels.extend(product_collections_list)

            for label in all_labels:
                # Open appropriate label(s).  
                print '- Label: {}'.format(label)
                print ' ... Opening Label ... '
                label_list = open_label(label.label())
                label_root = label_list
                # Build Alias
                print ' ... Building Label ... '
                label_root = alias.build_alias(label_root)
		#alias.alias_list.append(label_root)


                # Close appropriate label(s)
                print ' ... Closing Label ... '
                close_label(label.label(), label_root)

            #print alias.print_alias_list()

            print '---------------- End Build Alias -----------------------------------'  
	

        # Get all current Alias objects associated with the user's Bundle
        alias_list = Alias.objects.filter(bundle=bundle)
        context_dict['alias_list'] = alias_list
        return render(request, 'build/alias/alias.html',context_dict)
    else:
        print 'unauthorized user attempting to access a restricted area.'
        return redirect('main:restricted_access')









@login_required
def alias_delete(request, pk_bundle, alias):

    print ' \n\n \n\n-------------------------------------------------------------------------'
    print '\n\n---------------------- Remove an Alias with ELSA ---------------------------'
    print '------------------------------ DEBUGGER ---------------------------------'

    bundle = Bundle.objects.get(pk=pk_bundle)

    if request.user == bundle.user:
	print "authorized user"
        delete_alias = request.POST.get('Delete')


        context_dict = {
	    'alias':alias,
  	    'bundle':bundle,
	    'delete_alias':delete_alias,
        }

        print alias
        print request
        print bundle
    
        alias_class = Alias()

        if request.method == 'POST':
	    alias_class.remove(bundle, alias)
	    alias_to_remove = Alias.objects.filter(bundle=bundle).filter(alternate_id=alias)
	    alias_to_remove.delete()
	    return redirect('build:alias', pk_bundle = pk_bundle)

        return render(request, 'build/alias_delete/alias_delete.html',context_dict)

    else:
	print 'unauthorized user attempting to access a restricted area.'
        return redirect('main:restricted_access')







@login_required
def array(request, pk_bundle):
    print ' \n\n \n\n-------------------------------------------------------------------------'
    print '\n\n---------------- Welcome to Build A Bundle with ELSA --------------------'
    print '------------------------------ DEBUGGER ---------------------------------'

    bundle = Bundle.objects.get(pk=pk_bundle)

    if request.user == bundle.user:
        # Get forms
        form_array = ArrayForm(request.POST or None)

        # Declare context_dict for template
        context_dict = {
	    'bundle':bundle,
            'form_array':form_array,
        }

        # After ELSAs friend hits submit, if the forms are completed correctly, we should enter
        # this conditional.
        print '\n\n------------------------------- ARRAY INFO --------------------------------'
        print '\nCurrently awaiting user input...\n\n'
        if form_array.is_valid():
            print 'form_array is valid for {}.'.format(bundle.user)
            # Create Array model object
            array = form_array.save(commit=False)
            array.bundle = bundle
            array.save()
            print 'Array model object: {}'.format(array)

            # Find appropriate label(s).
            # Array gets added to... some... Product_Observational labels.
            # We first get all labels of these given types.
            all_labels = []

            for label in all_labels:
                # Open appropriate label(s).  
                print '- Label: {}'.format(label)
                print ' ... Opening Label ... '
                label_list = open_label(label.label())
                label_root = label_list
                # Build Array
                print ' ... Building Label ... '
                #label_root = array.build_array(label_root)
		#array.array_list.append(label_root) <~-- just stole this from alias ?? idk what does


                # Close appropriate label(s)
                print ' ... Closing Label ... '
                close_label(label.label(), label_root)

        return render(request, 'build/data/array.html', context_dict)

    else:
        print 'unauthorized user attempting to access a restricted area.'
        return redirect('main:restricted_access')



@login_required
def array(request, pk_bundle):
    print ' \n\n \n\n-------------------------------------------------------------------------'
    print '\n\n---------------- Welcome to Build A Bundle with ELSA --------------------'
    print '------------------------------ DEBUGGER ---------------------------------'

    bundle = Bundle.objects.get(pk=pk_bundle)

    if request.user == bundle.user:
        # Get forms
        form_array = ArrayForm(request.POST or None)

        # Declare context_dict for template
        context_dict = {
	    'bundle':bundle,
            'form_array':form_array,
        }

        # After ELSAs friend hits submit, if the forms are completed correctly, we should enter
        # this conditional.
        print '\n\n------------------------------- ARRAY INFO --------------------------------'
        print '\nCurrently awaiting user input...\n\n'
        if form_array.is_valid():
            print 'form_array is valid for {}.'.format(bundle.user)
            # Create Array model object
            array = form_array.save(commit=False)
            array.bundle = bundle
            array.save()
            print 'Array model object: {}'.format(array)

            # Find appropriate label(s).
            # Array gets added to... some... Product_Observational labels.
            # We first get all labels of these given types.
            all_labels = []

            for label in all_labels:
                # Open appropriate label(s).  
                print '- Label: {}'.format(label)
                print ' ... Opening Label ... '
                label_list = open_label(label.label())
                label_root = label_list
                # Build Array
                print ' ... Building Label ... '
                #label_root = array.build_array(label_root)
		#array.array_list.append(label_root) <~-- just stole this from alias ?? idk what does


                # Close appropriate label(s)
                print ' ... Closing Label ... '
                close_label(label.label(), label_root)

        return render(request, 'build/data/array.html', context_dict)

    else:
        print 'unauthorized user attempting to access a restricted area.'
        return redirect('main:restricted_access')







"""
    build is the start of the bundle building process.  Because a bundle has yet to be created, there is
    no security check to see if the user is associated with the bundle...
"""
@login_required
def build(request): 
    print ' \n\n \n\n-------------------------------------------------------------------------'
    print '\n\n---------------- Welcome to Build A Bundle with ELSA --------------------'
    print '------------------------------ DEBUGGER ---------------------------------'


    # Get forms
    form_bundle = BundleForm(request.POST or None)
    form_collections = CollectionsForm(request.POST or None)

    # Declare context_dict for template
    context_dict = {
        'form_bundle':form_bundle,
        'form_collections':form_collections,
        'user':request.user,
    }

    print '\n\n------------------------------- USER INFO -------------------------------'
    print 'User:    {}'.format(request.user)
    print 'Agency:  {}'.format(request.user.userprofile.agency)
    print 'All users have access to this area.'


    print '\n\n------------------------------- BUILD INFO --------------------------------'
    print '\n ... waiting on user input ...\n'
    # After ELSAs friend hits submit, if the forms are completed correctly, we should enter here
    # this conditional.
    if form_bundle.is_valid() and form_collections.is_valid():
        print 'form_bundle and form_collections are valid'

        # Check Uniqueness  --- GOTTA BE A BETTER WAY (k)
        bundle_name = form_bundle.cleaned_data['name']
        bundle_user = request.user
        bundle_count = Bundle.objects.filter(name=bundle_name, user=bundle_user).count()
        if bundle_count == 0: # If user and bundle name are unique, then...

            # Create Bundle model.
            bundle = form_bundle.save(commit=False)
	    #bundle.uniqueifier = bundle.name + "_" + str(request.user.id)
            bundle.user = request.user
            bundle.status = 'b' # b for build.  New Bundles are always in build stage first.
            bundle.save()
            print 'Bundle model object: {}'.format(bundle)

            # Build PDS4 Compliant Bundle directory in User Directory.
            bundle.build_directory()
            print 'Bundle directory: {}'.format(bundle.directory())

            # Create Product_Bundle model.
            product_bundle = ProductBundleForm().save(commit=False)
            product_bundle.bundle = bundle
            product_bundle.save()
            print 'product_bundle model object: {}'.format(product_bundle)

            # Build Product_Bundle label using the base case template found in
            # templates/pds4/basecase
            print '\n---------------Start Build Product_Bundle Base Case------------------------'
            product_bundle.build_base_case()  # simply copies basecase to user bundle directory
	    # Open label - returns a list where index 0 is the label object and 1 is the tree
            print ' ... Opening Label ... '
            label_list = open_label(product_bundle.label()) #list = [label_object, label_root]
            label_root = label_list
            # Fill label - fills
            print ' ... Filling Label ... '
            #label_root = bundle.version.fill_xml_schema(label_root)
            label_root = product_bundle.fill_base_case(label_root)
            # Close label
            print ' ... Closing Label ... '
            close_label(product_bundle.label(), label_root) 

            print '---------------- End Build Product_Bundle Base Case -------------------------'
  
            # Create Collections Model Object and list of Collections, list of Collectables
            collections = form_collections.save(commit=False)
            collections.bundle = bundle
            collections.save()
            print '\nCollections model object:    {}'.format(collections)

	    #Tell the bundle what data we have, from the collection form
	    if collections.has_raw_data is True:
		raw = Data(name = "data_raw", processing_level = "Raw", bundle = bundle)
		raw.save()
	    if collections.has_calibrated_data is True:
		calibrated = Data(name = "data_calibrated", processing_level = "Calibrated", bundle = bundle)
		calibrated.save()
	    if collections.has_derived_data is True:
		derived = Data(name = "data_derived", processing_level = "Derived", bundle = bundle)
		derived.save()
	    bundle.save()
            
            # Create PDS4 compliant directories for each collection within the bundle.            
            collections.build_directories()

            # Each collection in collections needs a model and a label
            for collection in collections.list():
                print collection

                # Create Product_Collection model for each collection
                product_collection = ProductCollectionForm().save(commit=False)
                product_collection.bundle = bundle
                if collection == 'document':
                    product_collection.collection = 'Document'
                elif collection == 'context':
                    product_collection.collection = 'Context'
                elif collection == 'xml_schema':
                    product_collection.collection = 'XML_Schema'
                elif collection == 'data':
                    product_collection.collection = 'Data'
                elif collection == 'browse':
                    product_collection.collection = 'Browse'
                elif collection == 'geometry':
                    product_collection.collection = 'Geometry'
                elif collection == 'calibration':
                    product_collection.collection = 'Calibration'
		elif collection == 'data_enum':
		    print "saw the data enum"
		    break
                product_collection.save()
                print '\n\n{} Collection Directory:    {}'.format(collection, product_collection.directory())

                # Build Product_Collection label for all labels other than those found in the data collection.
                print '-------------Start Build Product_Collection Base Case-----------------'
                if collection != 'data_raw' and collection != 'data_calibrated' and collection != 'data_derived':
                    product_collection.build_base_case()

                    # Open Product_Collection label
                    print ' ... Opening Label ... '
                    label_list = open_label(product_collection.label())
                    label_root = label_list

                    # Fill label
                    print ' ... Filling Label ... '
                    #label_root = bundle.version.fill_xml_schema(label_root)
                    label_root = product_collection.fill_base_case(label_root)

                    # Close label
                    print ' ... Closing Label ... '
                    close_label(product_collection.label(), label_root)
                    print '-------------End Build Product_Collection Base Case-----------------'
           
            # Further develop context_dict entries for templates            
            context_dict['Bundle'] = bundle
            context_dict['Product_Bundle'] = Product_Bundle.objects.get(bundle=bundle)
            context_dict['Product_Collection_Set'] = Product_Collection.objects.filter(bundle=bundle)

	    #url = str(bundle.id) +'/data_prep/'
	    url = str(bundle.id) +'/'
	    #url = 'two/'

            return redirect(url, request, context_dict)
            #return render(request, 'build/two.html', context_dict)

    return render(request, 'build/build.html', context_dict)


@login_required
def data_prep(request, bundle, data_enum):

    data = Data.objects.get(pk = bundle)
    bundle = Bundle.objects.get(pk = bundle)
    data_prep_form = DataPrepForm

    
    '''
The following two lines of code are confusing nonsense garbage that took me at least five weeks to figure
out, this is what they do as far as I understand. The first line creates a formset object using the data
prep form and the data prep model. It also prevents the bundle field from showing and makes triple sure
that it only shows the number of forms we want. The second line actually creates the formset that gets
displayed and gets the information for us using the formset object we just created. The first input is
the standard form stuff. The second input uses an object query to get the data_prep object associated
with the bundle  -J
    '''
    DataPrepFormSet = modelformset_factory(Data_Prep, data_prep_form, exclude=('bundle',) , extra=data.data_enum, max_num=data.data_enum, min_num=data.data_enum)
    formset = DataPrepFormSet(request.POST or None, queryset=Data_Prep.objects.filter(bundle=bundle))    

    context_dict = {
	'bundle':bundle,
	'DataPrepFormSet':DataPrepFormSet,
	'formset':formset,
    }

    print data.directory()

    if request.method == 'POST' and formset.is_valid():
	print "POST and valid"
	for form in formset:
		data_form = form.save()
		if data_form.name[:5] != "data_":
		    data_form.name = "data_"+data_form.name
		data_form.bundle = bundle

		#Create the actual data entries in the databasae
		print data_form.data_type
		if data_form.data_type == 'Table Delimited':
		    actual_data = Table_Delimited(name = data_form.name, bundle=bundle)
		    actual_data.save()
		elif data_form.data_type == 'Table Binary':
		    actual_data = Table_Binary(name = data_form.name, bundle=bundle)
		    actual_data.save()
		elif data_form.data_type == 'Table Fixed-Width':
		    actual_data = Table_Fixed_Width(name = data_form.name, bundle=bundle)
		    actual_data.save()

		# Create the data stubs
		data_form.build_data_directory()
		data_form.build_base_case()

		data_form.save()
	return render(request, 'build/two.html', context_dict)	

    return render(request, 'build/data_prep/data_prep.html', context_dict)








# The bundle_detail view is the page that details a specific bundle.
@login_required
def bundle(request, pk_bundle):
    # Get Bundle
    bundle = Bundle.objects.get(pk=pk_bundle)
    bundle_data = Data.objects.filter(bundle=pk_bundle)

    # Each data type get its own form as a way of hardcoding the data id for the data objects. It's 
    # inelegant but it's the easiest way I can think to do it without rewriting all of the data code again. 
    # This is explained in more detail when we use them. -J
    form_raw_data = DataObjectForm(request.POST or None)
    form_calibrated_data = DataObjectForm(request.POST or None)
    form_derived_data = DataObjectForm(request.POST or None)
    form_reduced_data = DataObjectForm(request.POST or None)

    # Get the data objects assiciated with the individual bundle data. The data_object querry is passed a
    # querry of the bundle_data for the associated processing level.
    raw_data_objects = Data_Object.objects.filter(data=bundle_data.filter(processing_level = "Raw"))
    calibrated_data_objects = Data_Object.objects.filter(data=bundle_data.filter(processing_level = "Calibrated"))
    derived_data_objects = Data_Object.objects.filter(data=bundle_data.filter(processing_level = "Derived"))
    reduced_data_objects = Data_Object.objects.filter(data=bundle_data.filter(processing_level = "Reduced"))
    

    # Secure ELSA by seeing if the user logged in is the same user associated with the Bundle
    if request.user == bundle.user:
        print 'authorized user: {}'.format(request.user)
        # ELSA's current user is the bundle user so begin view logic

        print ' \n\n \n\n----------------------------------------------------------------------\n'
        print '-----------------------BEGIN Bundle Detail VIEW--------------------------.\n'
        print '--------------------------------------------------------------------------\n'
        context_dict = {
            'bundle':bundle,
	    'bundle_data':bundle_data,
            'collections': Collections.objects.get(bundle=bundle),
	    'form_raw_data':form_raw_data,
	    'form_calibrated_data':form_calibrated_data,
	    'form_derived_data':form_derived_data,
	    'form_reduced_data':form_reduced_data,
	    'raw_data_objects':raw_data_objects,
	    'calibrated_data_objects':calibrated_data_objects,
	    'derived_data_objects':derived_data_objects,
	    'reduced_data_objects':reduced_data_objects,
        }

	# Each data type gets its own section (as stated above). This is done because there's no (simple)
	# way to get the data with the proper processing level to one dynamic form. It is possible that
	# there is a simple way around this that I overlooked. Until then try to keep the code compact.
	# Also for reference request.POST.get() gets the form based on the name provided in the submit
	# HTML tag. -J
	if request.method == 'POST': 
	    if request.POST.get("add_raw") and form_raw_data.is_valid():
	    	data = form_raw_data.save(commit = False)
	    	data.data = bundle_data.filter(processing_level = "Raw")[0]
		data.build_data_file()
	    	data.save()

	    if request.POST.get("add_calibrated") and form_calibrated_data.is_valid():
	   	data = form_calibrated_data.save(commit = False)
	    	data.data = bundle_data.filter(processing_level = "Calibrated")[0]
		data.build_data_file()
	    	data.save()

	    if request.POST.get("add_derived") and form_derived_data.is_valid():
	    	data = form_derived_data.save(commit = False)
	    	data.data = bundle_data.filter(processing_level = "Derived")[0]
		data.build_data_file()
	    	data.save()

	    if request.POST.get("add_reduced") and form_reduced_data.is_valid():
	    	data = form_reduced_data.save(commit = False)
	    	data.data = bundle_data.filter(processing_level = "Reduced")[0]
		data.build_data_file()
	    	data.save()
	   


        return render(request, 'build/bundle/bundle.html', context_dict)

    else:
        print 'unauthorized user attempting to access a restricted area.'
        return redirect('main:restricted_access')



# The bundle_download view is not a page.  When a user chooses to download a bundle, this 'view' manifests and begins the downloading process.
def bundle_download(request, pk_bundle):
    # Get Bundle
    bundle = Bundle.objects.get(pk=pk_bundle)

    # Secure ELSA by seeing if the user logged in is the same user associated with the Bundle
    if request.user == bundle.user:
        print 'authorized user: {}'.format(request.user)

        # ELSA's current user is the bundle user so begin view logic
        print '----------------------------------------------------------------------------------\n'
        print '------------------------------ START BUNDLE DOWNLOAD -----------------------------\n'
        print '----------------------------------------------------------------------------------\n'

        print '\n\n------------------------------- BUNDLE INFO -------------------------------'
        print 'Bundle User: {}'.format(bundle.user)
        print 'Bundle Directory: {}'.format(bundle.directory())
        print 'Current Working Directory: {}'.format(os.getcwd())
        print 'Temporary Directory: {}'.format(settings.TEMPORARY_DIR)
        print 'Archive Directory: {}'.format(settings.ARCHIVE_DIR)

        # Make tarfile
        #    Note: This does not run in build directory, it runs in the elsa project directory, where manage.py lives.  
        tar_bundle_dir = '{}.tar.gz'.format(bundle.directory())
        temp_dir = os.path.join(settings.TEMPORARY_DIR, tar_bundle_dir)
        source_dir = os.path.join(settings.ARCHIVE_DIR, bundle.user.username)
        source_dir = os.path.join(source_dir, bundle.directory())
        make_tarfile(temp_dir, source_dir)

        # Testing.  See if simply bundle directory will download.
        # Once finished, make directory a tarfile and then download.
        file_path = os.path.join(settings.TEMPORARY_DIR, tar_bundle_dir)


        if os.path.exists(file_path):
            with open(file_path, 'rb') as fh:
                response = HttpResponse(fh.read(), content_type="application/x-tar")
                response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
                return response

        return HttpResponse("Download did not work.")

    else:
        print 'unauthorized user attempting to access a restricted area.'
        return redirect('main:restricted_access')










# The bundle_delete view is the page a user sees once they select the delete bundle button.  This view gives the user an option to confirm or take back their choice.  This view could be improved upon.
@login_required
def bundle_delete(request, pk_bundle):


    # Get Bundle
    bundle = Bundle.objects.get(pk=pk_bundle)

    # Secure ELSA by seeing if the user logged in is the same user associated with the Bundle
    if request.user == bundle.user:
        print 'authorized user: {}'.format(request.user)

        # ELSA's current user is the bundle user so begin view logic
        print '\n\n'
        print '---------------------------------------------------------------------------------\n'
        print '---------------------- Start Bundle Delete --------------------------------------\n'
        print '---------------------------------------------------------------------------------\n'


        print '\n\n------------------------------- BUNDLE INFO -------------------------------'
        print 'Bundle: {}'.format(bundle)
        print 'User: {}'.format(bundle.user)
	print 'Request: {}'.format(request.user)

        confirm_form = ConfirmForm(request.POST or None)
        context_dict = {}
        context_dict['bundle'] = bundle
        context_dict['user'] = bundle.user
        context_dict['delete_bundle_form'] = confirm_form   # CHANGE CONTEXT_DICT KEY TO 'confirm_form' #
        context_dict['user_response'] = 'empty'


        print 'Form confirm_form is valid: {}'.format(confirm_form.is_valid())
        print 'Response user_response is: {}'.format(context_dict['user_response'])
        if confirm_form.is_valid():
            print 'Delete Bundle? {}'.format(confirm_form.cleaned_data["decision"])
            decision = confirm_form.cleaned_data['decision']
            if decision == 'Yes':
                context_dict['decision'] = 'was'
                success_status = bundle.remove_bundle()
		bundle.delete()
                if success_status:
                    return redirect('../../success_delete/')


            if decision == 'No':
                # Go back to bundle page
                context_dict['decision'] = 'was not'

        return render(request, 'build/bundle/confirm_delete.html', context_dict)

    # Secure: Current user is not the user associated with the bundle, so...
    else:
        print 'unauthorized user attempting to access a restricted area.'
        return redirect('main:restricted_access')


def success_delete(request):
    return render(request, 'build/bundle/success_delete.html')











def citation_information(request, pk_bundle):
    print '\n\n'
    print '-------------------------------------------------------------------------'
    print '\n\n--------------- Add Citation_Information with ELSA -------------------'
    print '------------------------------ DEBUGGER ---------------------------------'


    bundle = Bundle.objects.get(pk=pk_bundle)

    # Secure ELSA by seeing if the user logged in is the same user associated with the Bundle
    if request.user == bundle.user:
        print 'authorized user: {}'.format(request.user)

        # Get forms
        form_citation_information = CitationInformationForm(request.POST or None)

        # Declare context_dict for template
        context_dict = {
            'form_citation_information':form_citation_information,
            'bundle':bundle,

        }

        # After ELSAs friend hits submit, if the forms are completed correctly, we should enter
        # this conditional.
        print '\n\n----------------- CITATION_INFORMATION INFO -------------------------'
        if form_citation_information.is_valid():
            print 'form_citation_information is valid'
            # Create Citation_Information model object
            citation_information = form_citation_information.save(commit=False)
            citation_information.bundle = bundle
            citation_information.save()
            print 'Citation Information model object: {}'.format(citation_information)

            # Find appropriate label(s).  Citation_Information gets added to all Product_Bundle and 
            # Product_Collection labels in a Bundle.  The Data collection is excluded since it is 
            # handled different from the other collections.
            all_labels = []
            product_bundle = Product_Bundle.objects.get(bundle=bundle)
            product_collections_list = Product_Collection.objects.filter(bundle=bundle).exclude(collection='Data')
            all_labels.append(product_bundle)             # Append because a single item
            all_labels.extend(product_collections_list)   # Extend because a list

            for label in all_labels:

                # Open appropriate label(s).  
                print '- Label: {}'.format(label)
                print ' ... Opening Label ... '
                label_list = open_label(label.label())
                label_root = label_list
        
                # Build Citation Information
                print ' ... Building Label ... '
                label_root = citation_information.build_citation_information(label_root)

                # Close appropriate label(s)
                print ' ... Closing Label ... '
                close_label(label.label(), label_root)

                print '------------- End Build Citation Information -------------------'        
        # Update context_dict with the current Citation_Information models associated with the user's bundle
        context_dict['citation_information_set'] = Citation_Information.objects.filter(bundle=bundle)
        return render(request, 'build/citation_information/citation_information.html',context_dict)

    # Secure: Current user is not the user associated with the bundle, so...
    else:
        print 'unauthorized user attempting to access a restricted area.'
        return redirect('main:restricted_access')










def context_search(request, pk_bundle):
    print '\n\n'
    print '-------------------------------------------------------------------------'
    print '\n\n------------------- Context Search with ELSA ------------------------'
    print '------------------------------ DEBUGGER ---------------------------------'

    # Get bundle and collections
    bundle = Bundle.objects.get(pk=pk_bundle)
#    collections = Collections.objects.get(bundle=bundle)

    # Secure ELSA by seeing if the user logged in is the same user associated with the Bundle
    if request.user == bundle.user:
        print 'authorized user: {}'.format(request.user)

        # Context Dictionary
        context_dict = {
            'bundle':bundle,
            'investigation_list':bundle.investigations.all(),
            'instrument_host_list':bundle.instrument_hosts.all(),            
            'instrument_list':bundle.instruments.all(),
            'target_list':bundle.targets.all(),
            'facility_list':bundle.facilities.all(),
        }

        return render(request, 'build/context/context_search.html', context_dict)

    # Secure: Current user is not the user associated with the bundle, so...
    else:
        print 'unauthorized user attempting to access a restricted area.'
        return redirect('main:restricted_access')











def context_search_investigation(request, pk_bundle):
    print '\n\n'
    print '-------------------------------------------------------------------------'
    print '\n\n--------------- Add Context: Investigation with ELSA ----------------'
    print '------------------------------ DEBUGGER ---------------------------------'

    # Get bundle and collections
    bundle = Bundle.objects.get(pk=pk_bundle)

    # Secure ELSA by seeing if the user logged in is the same user associated with the Bundle
    if request.user == bundle.user:
        print 'authorized user: {}'.format(request.user)

        # Get form for observing system component
        form_investigation = InvestigationForm(request.POST or None)

        # Context Dictionary
        context_dict = {
            'bundle':bundle,
            'form_investigation':form_investigation,
            'bundle_investigation_set': bundle.investigations.all(),
        }

        # If the user just added an investigation, add it to the context dictionary
        # so we can notify the user it has been added
        if request.method == 'POST':
            if form_investigation.is_valid():
		print Investigation.objects.all()
                i = Investigation.objects.get(name=form_investigation.cleaned_data['investigation'])
                context_dict['investigation'] = i
                bundle.investigations.add(i)
		'''
	        fil = open('/home/tpagan/older ELSAs/elsa_kays_current/ELSA-online-master/archive/tpagan/jacobtest_bundle/document/collection_document.xml','r')

	        fileText = fil.read()

	        fil.close()
	
	        print fileText
		'''
		i.fill_label(bundle)


        return render(request, 'build/context/context_search_investigation.html', context_dict)

    # Secure: Current user is not the user associated with the bundle, so...
    else:
        print 'unauthorized user attempting to access a restricted area.'
        return redirect('main:restricted_access')











def context_search_instrument_host(request, pk_bundle, pk_investigation):
    print '\n\n'
    print '-------------------------------------------------------------------------'
    print '\n\n-------------- Add Context: Instrument Host with ELSA ---------------'
    print '------------------------------ DEBUGGER ---------------------------------'

    # Get bundle and collections
    bundle = Bundle.objects.get(pk=pk_bundle)
    investigation = Investigation.objects.get(pk=pk_investigation)

    # Secure ELSA by seeing if the user logged in is the same user associated with the Bundle
    if request.user == bundle.user:
        print 'authorized user: {}'.format(request.user)

        # Get form for observing system component
        form_instrument_host = InstrumentHostForm(request.POST or None, pk_inv=pk_investigation)

        # Context Dictionary
        context_dict = {
            'bundle':bundle,
            'investigation':investigation,
            'form_instrument_host':form_instrument_host,
            'bundle_instrument_host_set': bundle.instrument_hosts.all(), # We could add filters
        }
        
        # If the user just added an instrument host, add it to the context dictionary
        # so we can notify the user it has been added
        if request.method == 'POST':
            if form_instrument_host.is_valid():
                i = Instrument_Host.objects.get(name=form_instrument_host.cleaned_data['instrument_host'])
                context_dict['instrument_host'] = i
                bundle.instrument_hosts.add(i)
                i.fill_label(bundle)    
            
                
                        

        return render(request, 'build/context/context_search_instrument_host.html', context_dict)

    # Secure: Current user is not the user associated with the bundle, so...
    else:
        print 'unauthorized user attempting to access a restricted area.'
        return redirect('main:restricted_access')










def context_search_target(request, pk_bundle, pk_investigation, pk_instrument_host):
    print '\n\n'
    print '-------------------------------------------------------------------------'
    print '\n\n------------------- Add Context: Targets with ELSA ------------------'
    print '------------------------------ DEBUGGER ---------------------------------'

    # Get bundle and collections
    bundle = Bundle.objects.get(pk=pk_bundle)
    investigation = Investigation.objects.get(pk=pk_investigation)
    instrument_host = Instrument_Host.objects.get(pk=pk_instrument_host)

    # Secure ELSA by seeing if the user logged in is the same user associated with the Bundle
    if request.user == bundle.user:
        print 'authorized user: {}'.format(request.user)

        # Get form for observing system component
        form_target = TargetForm(request.POST or None, pk_ins=pk_instrument_host)

        # Context Dictionary
        context_dict = {
            'bundle':bundle,
            'investigation':investigation,
            'instrument_host':instrument_host,
            'form_target':form_target,
            'bundle_target_set': bundle.targets.all(), # We could add filters
        }
        
        # If the user just added an instrument host, add it to the context dictionary
        # so we can notify the user it has been added
        if request.method == 'POST':
            if form_target.is_valid():
                i = Target.objects.get(name=form_target.cleaned_data['target'])
                context_dict['target'] = i
                bundle.targets.add(i)
                i.fill_label(bundle)
                
                        

        return render(request, 'build/context/context_search_target.html', context_dict)

    # Secure: Current user is not the user associated with the bundle, so...
    else:
        print 'unauthorized user attempting to access a restricted area.'
        return redirect('main:restricted_access')










def context_search_instrument(request, pk_bundle, pk_investigation, pk_instrument_host):
    print '\n\n'
    print '-------------------------------------------------------------------------'
    print '\n\n--------------- Add Context: Instruments with ELSA ------------------'
    print '------------------------------ DEBUGGER ---------------------------------'

    # Get bundle and collections
    bundle = Bundle.objects.get(pk=pk_bundle)
    investigation = Investigation.objects.get(pk=pk_investigation)
    instrument_host = Instrument_Host.objects.get(pk=pk_instrument_host)

    # Secure ELSA by seeing if the user logged in is the same user associated with the Bundle
    if request.user == bundle.user:
        print 'authorized user: {}'.format(request.user)

        # Get form for observing system component
        form_instrument = InstrumentForm(request.POST or None, pk_ins=pk_instrument_host)

        # Context Dictionary
        context_dict = {
            'bundle':bundle,
            'investigation':investigation,
            'instrument_host':instrument_host,
            'form_instrument':form_instrument,
            'bundle_instrument_set': bundle.instruments.all(), # We could add filters
        }
        
        # If the user just added an instrument host, add it to the context dictionary
        # so we can notify the user it has been added
        if request.method == 'POST':
            if form_instrument.is_valid():
                i = Instrument.objects.get(name=form_instrument.cleaned_data['instrument'])
                context_dict['instrument'] = i
                bundle.instruments.add(i)
                i.fill_label(bundle)
                
                        

        return render(request, 'build/context/context_search_instrument.html', context_dict)

    # Secure: Current user is not the user associated with the bundle, so...
    else:
        print 'unauthorized user attempting to access a restricted area.'
        return redirect('main:restricted_access')







def context_search_facility(request, pk_bundle):
    print '\n\n'
    print '-------------------------------------------------------------------------'
    print '\n\n--------------- Add Context: Facility with ELSA ----------------'
    print '------------------------------ DEBUGGER ---------------------------------'

    # Get bundle and collections
    bundle = Bundle.objects.get(pk=pk_bundle)

    # Secure ELSA by seeing if the user logged in is the same user associated with the Bundle
    if request.user == bundle.user:
        print 'authorized user: {}'.format(request.user)

        # Get form for observing system component
        form_facility = FacilityForm(request.POST or None)

        # Context Dictionary
        context_dict = {
            'bundle':bundle,
            'form_facility':form_facility,
            'bundle_facility_set': bundle.facilities.all(),
        }

        # If the user just added an investigation, add it to the context dictionary
        # so we can notify the user it has been added
        if request.method == 'POST':
            if form_facility.is_valid():
                i = Facility.objects.get(name=form_facility.cleaned_data['facility'])
                context_dict['facility'] = i
		
		

                bundle.facilities.add(i)
                i.fill_label(bundle)


        return render(request, 'build/context/context_search_facility.html', context_dict)

    # Secure: Current user is not the user associated with the bundle, so...
    else:
        print 'unauthorized user attempting to access a restricted area.'
        return redirect('main:restricted_access')






def context_search_facility_instrument(request, pk_bundle, pk_facility):
    print '\n\n'
    print '-------------------------------------------------------------------------'
    print '\n\n--------------- Add Context: Instruments with ELSA ------------------'
    print '------------------------------ DEBUGGER ---------------------------------'

    # Get bundle and collections
    bundle = Bundle.objects.get(pk=pk_bundle)
    facility = Facility.objects.get(pk=pk_facility)
    
    # Secure ELSA by seeing if the user logged in is the same user associated with the Bundle
    if request.user == bundle.user:
        print 'authorized user: {}'.format(request.user)

        # Get form for observing system component
        form_instrument = FacilityInstrumentForm(request.POST or None, pk_fac=pk_facility)

        # Context Dictionary
        context_dict = {
            'bundle':bundle,
            'facility':facility,
            'form_instrument':form_instrument,
            'bundle_instrument_set': bundle.instruments.all(), # We could add filters
        }
        
        # If the user just added an instrument host, add it to the context dictionary
        # so we can notify the user it has been added
        if request.method == 'POST':
            if form_instrument.is_valid():
                i = Instrument.objects.get(name=form_instrument.cleaned_data['instrument'])
                context_dict['instrument'] = i
                bundle.instruments.add(i)
                i.fill_label(bundle)
                
                        

        return render(request, 'build/context/context_search_facility_instrument.html', context_dict)

    # Secure: Current user is not the user associated with the bundle, so...
    else:
        print 'unauthorized user attempting to access a restricted area.'
        return redirect('main:restricted_access')




def context_search_telescope(request, pk_bundle):
    print '\n\n'
    print '-------------------------------------------------------------------------'
    print '\n\n--------------- Add Context: Telescope with ELSA ----------------'
    print '------------------------------ DEBUGGER ---------------------------------'

    # Get bundle and collections
    bundle = Bundle.objects.get(pk=pk_bundle)

    # Secure ELSA by seeing if the user logged in is the same user associated with the Bundle
    if request.user == bundle.user:
        print 'authorized user: {}'.format(request.user)

        # Get form for observing system component
        form_telescope = TelescopeForm(request.POST or None)

        # Context Dictionary
        context_dict = {
            'bundle':bundle,
            'form_telescope':form_telescope,
            'bundle_telescope_set': bundle.telescopes.all(),
        }

        # If the user just added an investigation, add it to the context dictionary
        # so we can notify the user it has been added
        if request.method == 'POST':
            if form_telescope.is_valid():
                i = Telescope.objects.get(name=form_telescope.cleaned_data['telescope'])
                context_dict['telescope'] = i
                bundle.telescopes.add(i)


        return render(request, 'build/context/context_search_telescope.html', context_dict)

    # Secure: Current user is not the user associated with the bundle, so...
    else:
        print 'unauthorized user attempting to access a restricted area.'
        return redirect('main:restricted_access')





@login_required
def data(request, pk_bundle):
    print '\n\n'
    print '-------------------------------------------------------------------------'
    print '\n\n---------------------- Add Data with ELSA ---------------------------'
    print '------------------------------ DEBUGGER ---------------------------------'
    # Get bundle
    bundle = Bundle.objects.get(pk=pk_bundle)

    # Secure ELSA by seeing if the user logged in is the same user associated with the Bundle
    if request.user == bundle.user:
        print 'authorized user: {}'.format(request.user)

        # Context Dictionary
        context_dict = {
            'bundle':bundle,
        }
      
        return render(request, 'build/data/data.html', context_dict)

    # Secure: Current user is not the user associated with the bundle, so...
    else:
        print 'unauthorized user attempting to access a restricted area.'
        return redirect('main:restricted_access')


@login_required
def data_raw(request, pk_bundle):
    print '\n\n'
    print '-------------------------------------------------------------------------'
    print '\n\n---------------------- Add Data Raw with ELSA ---------------------------'
    print '------------------------------ DEBUGGER ---------------------------------'
    # Get bundle
    bundle = Bundle.objects.get(pk=pk_bundle)

    # Secure ELSA by seeing if the user logged in is the same user associated with the Bundle
    if request.user == bundle.user:
        print 'authorized user: {}'.format(request.user)

        # Context Dictionary
        context_dict = {
            'bundle':bundle,
        }
      
        return render(request, 'build/data/data_raw.html', context_dict)

    # Secure: Current user is not the user associated with the bundle, so...
    else:
        print 'unauthorized user attempting to access a restricted area.'
        return redirect('main:restricted_access')


@login_required
def data_raw(request, pk_bundle):
    print '\n\n'
    print '-------------------------------------------------------------------------'
    print '\n\n---------------------- Add Data Raw with ELSA ---------------------------'
    print '------------------------------ DEBUGGER ---------------------------------'
    # Get bundle
    bundle = Bundle.objects.get(pk=pk_bundle)

    # Secure ELSA by seeing if the user logged in is the same user associated with the Bundle
    if request.user == bundle.user:
        print 'authorized user: {}'.format(request.user)

        # Context Dictionary
        context_dict = {
            'bundle':bundle,
        }
      
        return render(request, 'build/data/data_raw.html', context_dict)

    # Secure: Current user is not the user associated with the bundle, so...
    else:
        print 'unauthorized user attempting to access a restricted area.'
        return redirect('main:restricted_access')

@login_required
def data_depricated(request, pk_bundle): 
    print '\n\n'
    print '-------------------------------------------------------------------------'
    print '\n\n---------------------- Add Data with ELSA ---------------------------'
    print '------------------------------ DEBUGGER ---------------------------------'

    # Get bundle
    bundle = Bundle.objects.get(pk=pk_bundle)

    # Secure ELSA by seeing if the user logged in is the same user associated with the Bundle
    if request.user == bundle.user:
        print 'authorized user: {}'.format(request.user)

        # Get forms
        form_data = DataForm(request.POST or None)
        form_product_observational = ProductObservationalForm(request.POST or None)

        # Context Dictionary
        context_dict = {
            'bundle':bundle,
            'form_data':form_data,
            'form_product_observational':form_product_observational,
        }
        # After ELSAs friend hits submit, if the forms are completed correctly, we should enter
        # this conditional.
        print '\n\n------------------------ DATA INFO ----------------------------------'
        if form_data.is_valid() and form_product_observational.is_valid():

            # Create Data model object
            data = form_data.save(commit=False)
            data.bundle = bundle
            data.save()
            print 'Data model object: {}'.format(data)

            # Create Product_Observational model object
            product_observational = form_product_observational.save(commit=False)
            product_observational.bundle = bundle
            product_observational.data = data
            product_observational.processing_level = data.processing_level
            product_observational.save()
            print 'Product_Observational model object: {}'.format(product_observational)

            # Create Data Folder corresponding to processing level
            data.build_directory()

            print '---------------- Start Build Product_Collection Base Case ------------------------'
            product_collection = Product_Collection.objects.get(bundle=bundle, collection='Data')
            product_collection.build_base_case_data(data)
        
            print '---------------- End Build Product_Collection Base Case -------------------------'
                


            print '---------------- Start Build Product_Observational Base Case ---------------------'
            # Copy Product_Observational label
            product_observational.build_base_case()

            # Open label - returns a list of label information where list = [label_object, label_root]
            print ' ... Opening Label ... '
            label_list = open_label(product_observational.label())
            label_root = label_list
            # Fill label - fills 
            print ' ... Filling Label ... '
            label_root = product_observational.fill_base_case(label_root)
            # Close label
            print ' ... Closing Label ... '
            close_label(product_observational.label(), label_root)           
            print '---------------- End Build Product_Observational Base Case-----------------------'

            # Update context_dict
            print '\n\n---------------------- UPDATING CONTEXT DICTIONARY --------------------------'
            context_dict['data'] = data
            context_dict['product_observational'] = product_observational  # Needs a fix
        
        data_set = Data.objects.filter(bundle=bundle)
        context_dict['data_set'] = data_set
        product_observational_set = []
        for data in data_set:
            product_observational_set.extend(Product_Observational.objects.filter(data=data))
        context_dict['product_observational_set'] = product_observational_set
      
        return render(request, 'build/data/data.html', context_dict)

    # Secure: Current user is not the user associated with the bundle, so...
    else:
        print 'unauthorized user attempting to access a restricted area.'
        return redirect('main:restricted_access')




@login_required
def display_dictionary(request, pk_bundle):
    print ' \n\n \n\n-------------------------------------------------------------------------'
    print '\n\n------------------- Add Display Dictionary with ELSA --------------------------'
    print '------------------------------ DEBUGGER ---------------------------------'

    # Get Bundle
    bundle = Bundle.objects.get(pk=pk_bundle)
#    collections = Collections.objects.get(bundle=bundle)

    # Secure ELSA by seeing if the user logged in is the same user associated with the Bundle
    if request.user == bundle.user:
        print 'authorized user: {}'.format(request.user)

        # ELSA's current user is the bundle user so begin view logic
        # Get forms
        form_color_display_settings = ColorDisplaySettingsForm(request.POST or None)
        form_display_direction = DisplayDirectionForm(request.POST or None)
        form_display_settings = DisplaySettingsForm(request.POST or None)
        form_movie_display_settings = MovieDisplaySettingsForm(request.POST or None)

        # Declare context_dict for templating language used in ELSAs templates
        context_dict = {
            'bundle':bundle,
            'form_color_display_settings':form_color_display_settings,
            'form_display_direction':form_display_direction,
            'form_display_settings':form_display_settings,
            'form_movie_display_settings':form_movie_display_settings,

        }

        # After ELSAs friend hits submit, if the forms are completed correctly, we should enter
        # this conditional.
        print '\n\n------------------------ DISPLAY DICTIONARY INFO ----------------------------'
        print '\nCurrently awaiting user input...\n\n'
        if form_color_display_settings.is_valid() and form_display_direction.is_valid() and form_display_settings.is_valid() and form_movie_display_settings.is_valid():

            print 'All Display Dictionary forms valid for {}.'.format(bundle.user)
            # Create DisplayDictionary model object
            display_dictionary = form_display_dictionary.save(commit=False)
            display_dictionary.bundle = bundle
            display_dictionary.save()
            print 'Display Dictionary model object: {}'.format(display_dictionary)

            # Create Color_Display_Settings model object
            color_display_settings = form_color_display_settings.save(commit=False)
            # Add association
            color_display_settings.save()

            # Create Display_Direction model object
            display_direction = form_display_direction.save(commit=False)
            # Add association
            display_direction.save()

            # Create Display_Settings model object
            display_settings = form_display_settings.save(commit=False)
            # Add association
            display_settings.save()

            # Create Movie_Display_Direction model object
            movie_display_settings = form_movie_display_settings.save(commit=False)
            # Add association
            movie_display_settings.save()





            # Find appropriate label(s).
            print '---------------- End Build Display Dictionary ------------------------------'  
	

        # Get current Display Dictionary object associated with the user's Bundle
        #alias_list = Alias.objects.filter(bundle=bundle)
        #context_dict['alias_list'] = alias_list
        return render(request, 'build/dictionary/display.html',context_dict)
    else:
        print 'unauthorized user attempting to access a restricted area.'
        return redirect('main:restricted_access')














def document(request, pk_bundle):
    print '\n\n'
    print '-------------------------------------------------------------------------'
    print '\n\n--------------------- Add Document with ELSA ------------------------'
    print '------------------------------ DEBUGGER ---------------------------------'

    # Get bundle
    bundle = Bundle.objects.get(pk=pk_bundle)
#    collections = Collections.objects.get(bundle=bundle)

    # Secure ELSA by seeing if the user logged in is the same user associated with the Bundle
    if request.user == bundle.user:
        print 'authorized user: {}'.format(request.user)

        # Get forms
        form_product_document = ProductDocumentForm(request.POST or None)

        # Declare context_dict for template
        context_dict = {
            'form_product_document':form_product_document,
            'bundle':bundle,

        }

        # After ELSAs friend hits submit, if the forms are completed correctly, we should enter
        # this conditional.  We must do [] things: 1. Create the Document model object, 2. Add a Product_Document label to the Document Collection, 3. Add the Document as an Internal_Reference to the proper labels (like Product_Bundle and Product_Collection).
        print '\n\n---------------------- DOCUMENT INFO -------------------------------'
        if form_product_document.is_valid():
            print 'form_product_document is valid'  

            # Create Document Model Object
            product_document = form_product_document.save(commit=False)
            product_document.bundle = bundle
            product_document.save()
            print 'Product_Document model object: {}'.format(product_document)

            # Build Product_Document label using the base case template found
            # in templates/pds4/basecase
            print '\n---------------Start Build Product_Document Base Case------------------------'
            product_document.build_base_case()
            # Open label - returns a list where index 0 is the label object and 1 is the tree
            print ' ... Opening Label ... '
            label_list = open_label(product_document.label())
            label_root = label_list
            # Fill label - fills 
            print ' ... Filling Label ... '
            #label_root = bundle.version.fill_xml_schema(label_root)
            label_root = product_document.fill_base_case(label_root)
            # Close label    
            print ' ... Closing Label ... '
            close_label(label_object, label_root)          
            print '---------------- End Build Product_Document Base Case -------------------------' 

            # Add Document info to proper labels.  For now, I simply have Product_Bundle and Product_Collection with a correction for the data collection.  The variable all_labels_kill_data means all Product_Collection labels except those associated with data.  Further below, you will see the correction for the data collection where our label set is now data_labels.
            print '\n---------------Start Build Internal_Reference for Document-------------------'
            all_labels = []
            product_bundle = Product_Bundle.objects.get(bundle=bundle)
            product_collections_list = Product_Collection.objects.filter(bundle=bundle)

            all_labels.append(product_bundle)
            all_labels.extend(product_collections_list)  

            for label in all_labels:
                print '- Label: {}'.format(label)
                print ' ... Opening Label ... '
                label_list = open_label(label.label())
                label_root = label_list
        
                # Build Internal_Reference
                print ' ... Building Internal_Reference ... '
                label_root = label.build_internal_reference(label_root, product_document)

                # Close appropriate label(s)
                print ' ... Closing Label ... '
                close_label(label.label(), label_root)
            print '\n----------------End Build Internal_Reference for Document-------------------'


        context_dict['documents'] = Product_Document.objects.filter(bundle=bundle)    
        return render(request, 'build/document/document.html',context_dict)

    # Secure: Current user is not the user associated with the bundle, so...
    else:
        print 'unauthorized user attempting to access a restricted area.'
        return redirect('main:restricted_access')

 


 

def product_document(request, pk_bundle, pk_product_document):
    print '\n\n'
    print '-------------------------------------------------------------------------'
    print '\n\n------------------ Add Product_Document with ELSA -------------------'
    print '------------------------------ DEBUGGER ---------------------------------'
    # Get bundle
    bundle = Bundle.objects.get(pk=pk_bundle)

    # Secure ELSA by seeing if the user logged in is the same user associated with the Bundle
    if request.user == bundle.user:
        print 'authorized user: {}'.format(request.user)

        product_document = Product_Document.objects.get(pk=pk_product_document)
        context_dict = {
            'bundle':bundle,
            'product_observational':product_observational,
        }

        return render(request, 'build/document/product_document.html', context_dict)

    # Secure: Current user is not the user associated with the bundle, so...
    else:
        print 'unauthorized user attempting to access a restricted area.'
        return redirect('main:restricted_access')










def product_observational(request, pk_bundle, pk_product_observational):
    print '\n\n'
    print '-------------------------------------------------------------------------'
    print '\n\n---------------- Add Product_Observational with ELSA ----------------'
    print '------------------------------ DEBUGGER ---------------------------------'


    # Get bundle
    bundle = Bundle.objects.get(pk=pk_bundle)

    # Secure ELSA by seeing if the user logged in is the same user associated with the Bundle
    if request.user == bundle.user:
        print 'authorized user: {}'.format(request.user)

        product_observational = Product_Observational.objects.get(pk=pk_product_observational)
        form_product_observational = TableForm(request.POST or None)
        context_dict = {
            'bundle':bundle,
            'product_observational':product_observational,
            'form_product_observational':form_product_observational,

        }

        print '\n\n----------------- PRODUCT_DOCUMENT INFO -----------------------------'
        if form_product_observational.is_valid():
            print 'form_product_observational is valid.'
            # Create the associated model (Table, Array, Cube, etc...)
            observational = form_product_observational.save(commit=False)
            observational.product_observational = product_observational
            observational.save()
            print 'observational object: {}'.format(observational)
        

            print '\n--------- Start Add Observational to Product_Observational -----------------'
            # Open label
            print ' ... Opening Label ... '
            label_list = open_label(product_observational.label())
            label_object = label_list[0]
            label_root = label_list[1]
            print label_root

            # Fill label
            print ' ... Filling Label ... '
            #label_root = bundle.version.fill_xml_schema(label_root)
            label_root = product_observational.fill_observational(label_root, observational)

            # Close label
            print ' ... Closing Label ... '
            close_label(label_object, label_root)
            print '-------------End Add Observational to Product_Observational -----------------'
        
        # Now we must grab the observational set to display on ELSA's template for the Product_Observational page.  Right now, this is tables so it is easy.
        observational_set = Table.objects.filter(product_observational=product_observational)
        context_dict['observational_set'] = observational_set
    
        return render(request, 'build/data/table.html', context_dict)

    # Secure: Current user is not the user associated with the bundle, so...
    else:
        print 'unauthorized user attempting to access a restricted area.'
        return redirect('main:restricted_access')


def Table_Creation(request, data_object, pk_bundle):

    bundle = Bundle.objects.get(pk=pk_bundle)
    data_object = Data_Object.objects.get(pk=data_object)
    data_form = Table_Delimited_Form(request.POST or None)

    if request.user == bundle.user:

	if data_object.data_type == 'Table Delimited':
	    data_form = Table_Delimited_Form(request.POST or None)
	elif data_object.data_type == 'Table Binary':
	    data_form = Table_Binary_Form(request.POST or None)
	elif data_object.data_type == 'Table Fixed-Width':
	    data_form = Table_Fixed_Width_Form(request.POST or None)
	elif data_object.data_type == 'Array':
	    data_form = ArrayForm(request.POST or None)

	context_dict = {
	    'bundle':bundle,
	    'data_object':data_object,
	    'data_form':data_form,
	}

	if data_form.is_valid():
    	    form = data_form.save(commit=False)
	    form.name = data_object.name
	    form.save()
	    
	

	return render(request, 'build/data/Table_Creation.html', context_dict)
    else:
	print 'unauthorized user attempting to access a restricted area.'
        return redirect('main:restricted_access')


'''
def Table_Creation(request, pk_bundle):

    bundle = Bundle.objects.get(pk=pk_bundle)

    if request.user == bundle.user:


	#Count the number of tables of each type the bundle has. 
	#There's almost certainly a better way to do this, but this was faster and more reliable
	#than dreging the django API.
	TD_iterator = 0
	TB_iterator = 0
	TFW_iterator = 0

	tableTypes = Data_Prep.objects.filter(bundle=bundle)

	for table in tableTypes:
	    if table.data_type == "Table Delimited":
		TD_iterator = TD_iterator + 1
	    if table.data_type == "Table Binary":
		TB_iterator = TB_iterator + 1
	    if table.data_type == "Table Fixed-Width":
		TFW_iterator = TFW_iterator + 1

	#Create the formsets for each table.
        TableDelimitedFormSet = modelformset_factory(Table_Delimited, exclude=('bundle',) , extra=TD_iterator, max_num=TD_iterator)


	TableBinaryFormSet = modelformset_factory(Table_Binary, exclude=('bundle',) , extra=TB_iterator, max_num=TB_iterator)


	TableFixedWidthFormSet = modelformset_factory(Table_Fixed_Width, exclude=('bundle',) , extra=TFW_iterator, max_num=TFW_iterator)


	if request.method == 'POST':
            TD_formset = TableDelimitedFormSet(request.POST, queryset=Table_Delimited.objects.filter(bundle=bundle), prefix='delimited')
            TB_formset = TableBinaryFormSet(request.POST, queryset=Table_Binary.objects.filter(bundle=bundle), prefix='binary')
            TFW_formset = TableFixedWidthFormSet(request.POST, queryset=Table_Fixed_Width.objects.filter(bundle=bundle), prefix='character')
	else:
            TD_formset = TableDelimitedFormSet(queryset=Table_Delimited.objects.filter(bundle=bundle),prefix='delimited')
            TB_formset = TableBinaryFormSet(queryset=Table_Binary.objects.filter(bundle=bundle),prefix='binary')
            TFW_formset = TableFixedWidthFormSet(queryset=Table_Fixed_Width.objects.filter(bundle=bundle),prefix='character')


	context_dict = {
	    'bundle':bundle,
	    'TableDelimitedFormSet':TableDelimitedFormSet,
	    'TD_formset':TD_formset,
	    'TD_iterator':TD_iterator,
	    'TableBinaryFormSet':TableBinaryFormSet,
	    'TB_formset':TB_formset,
	    'TB_iterator':TB_iterator,
	    'TableFixedWidthFormSet':TableFixedWidthFormSet,
	    'TFW_formset':TFW_formset,
	    'TFW_iterator':TFW_iterator,
	}



	#id_iterator = 0
	if request.method == 'POST':
	    #Create and fill the database fields as well as (eventually) filling the data files
	    #print str(TD_iterator) + " " + str(TD_formset.errors)
	    if TD_formset.is_valid() and request.method == 'POST':
	        id_iterator = 0
	    	for TD_form in TD_formset:
		    if TD_form.is_valid():
			print TD_form.data
  		    	table_id = TD_form.data['delimited-'+str(id_iterator)+'-id'] #Get Table object id
		    	print table_id
			print TD_form.data
		     	table = Table_Delimited.objects.get(id=table_id) #Get the actual Table object using the id from the previous step
		    	name = table.name #Get the Tables name (set in data_prep) using the object from the previous step
		    	table_form = TD_form.save()
		   	table_form.name = name #Manually fill the form name
		    	table_form.save()
		    	id_iterator = id_iterator+1


	    #print str(TB_iterator) + " " + str(TB_formset.errors)
	    if TB_formset.is_valid() and request.method == 'POST':
	     	id_iterator = 0
	    	for TB_form in TB_formset:
		    if TB_form.is_valid():
			print TB_form.data
		    	table_id = TB_form.data['binary-'+str(id_iterator)+'-id']
		    	print table_id

		    	table = Table_Binary.objects.get(id=table_id)
		    	name = table.name
		    	table_form = TB_form.save(commit=False)
		    	table_form.name = name
		    	table_form.save()
		    	id_iterator = id_iterator+1


	    #print str(TFW_iterator) + " " + str(TFW_formset.errors)
	    if TFW_formset.is_valid() and request.method == 'POST':
	    	id_iterator = 0
	    	for TFW_form in TFW_formset:
		    if TFW_form.is_valid():
		     	table_id = TFW_form.data['character-'+str(id_iterator)+'-id']
		    	print table_id
			print TFW_form.data
		    	table = Table_Fixed_Width.objects.get(id=table_id)
		    	name = table.name
		    	table_form = TFW_form.save(commit=False)
		    	table_form.name = name
		    	table_form.save()
		    	id_iterator = id_iterator+1


	

	return render(request, 'build/data/table_creation.html', context_dict)
    else:
	print 'unauthorized user attempting to access a restricted area.'
        return redirect('main:restricted_access')
'''

# Field Creation takes a table reference and a table type in order to get the properly associated Table Object 

def Field_Creation(request, pk_bundle, pk_table, table_type):

    bundle = Bundle.objects.get(pk=pk_bundle)

    if table_type is "Table Delimited":
        table = Table_Delimited.objects.get(pk=pk_table)
    elif table_type is "Table Binary":
	table = Table_Binary.objects.get(pk=pk_table)
    elif table_type is "Table Fixed Width":
	table = Table_Fixed_Width.objects.get(pk=pk_table)
    else:
	raise Exception(table_type + "is an unknown table type")
	return

    if request.user == bundle.user:
	pass
    else:
	print 'unauthorized user attempting to access a restricted area.'
        return redirect('main:restricted_access')
 

    


"""
    Context Views
"""


@login_required
def context(request):
    context_dict = {
    }

    return render(request, 'context/repository/repository.html', context_dict)


#@login_required
def investigations(request):
    context_dict = {
        'investigations':Investigation.objects.all(),
    }

    return render(request, 'context/repository/investigations.html', context_dict)


#@login_required
def instrument_hosts(request):
    context_dict = {
        'instrument_hosts':Instrument_Host.objects.all(),
    }

    return render(request, 'context/repository/instrument_hosts.html', context_dict)

#@login_required
def instruments(request):
    context_dict = {
        'instruments':Instrument.objects.all(),
    }

    return render(request, 'context/repository/instruments.html', context_dict)


























