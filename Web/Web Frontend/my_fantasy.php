<head>
<link rel="stylesheet" type="text/css" href="css/jquery.dataTables.css">
<script src="js/jquery-datatables.js"></script>
<script src="js/jquery.dataTables.js"></script>

</head>
<script>
//
// Updates "Select all" control in a data table
//
function updateDataTableSelectAllCtrl(table){
   var $table             = table.table().node();
   var $chkbox_all        = $('tbody input[type="checkbox"]', $table);
   var $chkbox_checked    = $('tbody input[type="checkbox"]:checked', $table);
   var chkbox_select_all  = $('thead input[name="select_all"]', $table).get(0);

   // If none of the checkboxes are checked
   if($chkbox_checked.length === 0){
      chkbox_select_all.checked = false;
      if('indeterminate' in chkbox_select_all){
         chkbox_select_all.indeterminate = false;
      }

   // If all of the checkboxes are checked
   } else if ($chkbox_checked.length === $chkbox_all.length){
      chkbox_select_all.checked = true;
      if('indeterminate' in chkbox_select_all){
         chkbox_select_all.indeterminate = false;
      }

   // If some of the checkboxes are checked
   } else {
      chkbox_select_all.checked = true;
      if('indeterminate' in chkbox_select_all){
         chkbox_select_all.indeterminate = true;
      }
   }
}

$(document).ready(function (){
   // Array holding selected row IDs
   var rows_selected = [];
   var table = $('#example').DataTable({
      'ajax': {
         'url': 'get_players.php' 

      },
      "pageLength": 100,
      'columnDefs': [{
         'targets': 0,
         'searchable': false,
         'orderable': false,
         'width': '1%',
         'className': 'dt-body-center',
         'render': function (data, type, full, meta){
             // playeridsalert(data);
             return '<input type="checkbox">';
         }
      }],
      'order': [[1, 'asc']],
      'rowCallback': function(row, data, dataIndex){
         // Get row ID
         var rowId = data[0];
         // If row ID is in the list of selected row IDs
         if($.inArray(rowId, rows_selected) !== -1){
            $(row).find('input[type="checkbox"]').prop('checked', true);
            $(row).addClass('selected');
         }
      }
   });

   // Handle click on checkbox
   $('#example tbody').on('click', 'input[type="checkbox"]', function(e){
      var $row = $(this).closest('tr');

      // Get row data
      var data = table.row($row).data();

      // Get row ID
      var rowId = data[0];

      // Determine whether row ID is in the list of selected row IDs 
      var index = $.inArray(rowId, rows_selected);

      // If checkbox is checked and row ID is not in list of selected row IDs
      if(this.checked && index === -1){
         rows_selected.push(rowId);

      // Otherwise, if checkbox is not checked and row ID is in list of selected row IDs
      } else if (!this.checked && index !== -1){
         rows_selected.splice(index, 1);
      }

      if(this.checked){
         $row.addClass('selected');
      } else {
         $row.removeClass('selected');
      }

      // Update state of "Select all" control
      updateDataTableSelectAllCtrl(table);

      // Prevent click event from propagating to parent
      e.stopPropagation();
   });

   // Handle click on table cells with checkboxes
   $('#example').on('click', 'tbody td, thead th:first-child', function(e){
      $(this).parent().find('input[type="checkbox"]').trigger('click');
   });

   // Handle click on "Select all" control
   $('thead input[name="select_all"]', table.table().container()).on('click', function(e){
      if(this.checked){
         $('#example tbody input[type="checkbox"]:not(:checked)').trigger('click');
      } else {
         $('#example tbody input[type="checkbox"]:checked').trigger('click');
      }

      // Prevent click event from propagating to parent
      e.stopPropagation();
   });

   // Handle table draw event
   table.on('draw', function(){
      // Update state of "Select all" control
      updateDataTableSelectAllCtrl(table);
   });

   // Handle form submission event 
   $('#add-player').on('submit', function(e){
      var form = this;
       
      // Iterate over all selected checkboxes
      $.each(rows_selected, function(index, rowId){
         // Create a hidden element 
         $(form).append(
             $('<input>')
                .attr('type', 'hidden')
                .attr('name', 'id[]')
                .val(rowId)
         );
      });
      alert($(this).serialize());
   });

});
</script>
<div id="content">

<form name="add-player" id="add-player" action="add_team.php">

<table id="example" class="display select" cellspacing="0" width="100%">

   <thead>

      <tr>

         <th><input name="select_all" value="1" type="checkbox"></th>
         <th>First Name</th>
         <th>Last Name</th>
         <th>Weight</th>
         <th>Height</th>
         <th>Bats</th>
         <th>Throws</th>
	 <th>Team ID</th>
      </tr>

   </thead>
   <tfoot>
      <tr>
         <th></th>
         <th>First Name</th>
         <th>Last Name</th>
         <th>Weight</th>
         <th>Height</th>
         <th>Bats</th>
         <th>Throws</th>
	 <th>Team ID</th>
      </tr>
   </tfoot>

</table>



<p class="form-group">

   <button type="submit" class="btn btn-primary">Submit</button>

</p>



<p class="form-group">

   <b>Data submitted to the server:</b>

   <pre id="example-console"></pre>

</p>



</form>

</div>


</div>
