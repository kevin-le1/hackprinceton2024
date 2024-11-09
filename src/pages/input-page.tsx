import * as React from 'react';
import { alpha } from '@mui/material/styles';
import Box from '@mui/material/Box';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TablePagination from '@mui/material/TablePagination';
import TableRow from '@mui/material/TableRow';
import TableSortLabel from '@mui/material/TableSortLabel';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import Paper from '@mui/material/Paper';
import Checkbox from '@mui/material/Checkbox';
import IconButton from '@mui/material/IconButton';
import Tooltip from '@mui/material/Tooltip';
import FormControlLabel from '@mui/material/FormControlLabel';
import Switch from '@mui/material/Switch';
import DeleteIcon from '@mui/icons-material/Delete';
import AddIcon from '@mui/icons-material/Add';
import { visuallyHidden } from '@mui/utils';
import TextField from '@mui/material/TextField'; 
import {api} from "../api/api";

interface Data {
  id: number;
  name: string;
  BMI: string;
  HR: string;
  BP: string;
  patientRisk: any;
  specialist: string;
  uuid: string;
}

function createData(
  id: number,
  name: any,
  BMI: any,
  HR: any,
  BP: any,
  patientRisk: any,
  specialist: any,
  uuid: string,
): Data {
  return {
    id,
    name,
    BMI,
    HR,
    BP,
    patientRisk,
    specialist,
    uuid
  };
}

// const rows = [
//   createData(1, 'John', "305", 3.7, "hi"),
//   createData(2, 'Carter', "452", 25.0),
//   createData(3, 'x', "262", 16.0),
//   createData(4, 'x', "159", 6.0),
//   createData(5, 'x', "356", 16.0),
//   createData(6, 'x', "408", 3.2),
//   createData(7, 'x', "237", 9.0),
//   createData(8, 'x', "375", 0.0),
// ];

interface HeadCell {
  disablePadding: boolean;
  id: keyof Data;
  label: string;
  numeric: boolean;
}

const headCells: readonly HeadCell[] = [
  {
    id: 'name',
    numeric: false,
    disablePadding: true,
    label: 'Patient Name',
  },
  {
    id: 'BMI',
    numeric: true,
    disablePadding: false,
    label: 'BMI',
  },
  {
    id: 'HR',
    numeric: true,
    disablePadding: false,
    label: 'HR',
  },
  {
    id: 'BP',
    numeric: true,
    disablePadding: false,
    label: 'BPM',
  },
  {
    id: 'specialist',
    numeric: true,
    disablePadding: false,
    label: 'Specialist',
  },
  {
    id: 'patientRisk',
    numeric: true,
    disablePadding: false,
    label: 'Patient Risk',
  },
];

interface EnhancedTableProps {
  numSelected: number;
  onSelectAllClick: (event: React.ChangeEvent<HTMLInputElement>) => void;
  rowCount: number;
}

function EnhancedTableHead(props: EnhancedTableProps) {
  const { onSelectAllClick, numSelected, rowCount } =
    props;

  return (
    <TableHead>
      <TableRow>
        <TableCell padding="checkbox">
          <Checkbox
            color="primary"
            indeterminate={numSelected > 0 && numSelected < rowCount}
            checked={rowCount > 0 && numSelected === rowCount}
            onChange={onSelectAllClick}
            inputProps={{
              'aria-label': 'select all desserts',
            }}
          />
        </TableCell>
        {headCells.map((headCell) => (
          <TableCell
            key={headCell.id}
            align={headCell.numeric ? 'right' : 'left'}
            padding={headCell.disablePadding ? 'none' : 'normal'}
          >
            <TableSortLabel
            >
              {headCell.label}
              {(
                <Box component="span" sx={visuallyHidden}>
                </Box>
              )}
            </TableSortLabel>
          </TableCell>
        ))}
      </TableRow>
    </TableHead>
  );
}
interface EnhancedTableToolbarProps {
  numSelected: number;
}
function EnhancedTableToolbar(props: EnhancedTableToolbarProps & { addRow: () => void, deleteRow: () => void }) {
  const { numSelected, addRow, deleteRow } = props;

  const handleAddRow = () => {
    addRow();
  };

  const handleDeleteRow = () => {
    deleteRow();
  };

  return (
    <Toolbar
      sx={[
        {
          pl: { sm: 2 },
          pr: { xs: 1, sm: 1 },
        },
        numSelected > 0 && {
          bgcolor: (theme) =>
            alpha(theme.palette.primary.main, theme.palette.action.activatedOpacity),
        },
      ]}
    >
      {numSelected > 0 ? (
        <Typography
          sx={{ flex: '1 1 100%' }}
          color="inherit"
          variant="subtitle1"
          component="div"
        >
          {numSelected} selected
        </Typography>
      ) : (
        <Typography
          sx={{ flex: '1 1 100%' }}
          variant="h6"
          id="tableTitle"
          component="div"
        >
          Patient Information
        </Typography>
      )}

        <Tooltip title="Add">
          <IconButton onClick={handleAddRow}>
            <AddIcon />
          </IconButton>
        </Tooltip>
      
        <Tooltip title="Delete">
          <IconButton onClick={handleDeleteRow}>
            <DeleteIcon />
          </IconButton>
        </Tooltip>
      
    </Toolbar>
  );
}


export default function Input() {
  const [selected, setSelected] = React.useState<readonly number[]>([]);
  const [page, setPage] = React.useState(0);
  const [dense, setDense] = React.useState(false);
  const [rowsPerPage, setRowsPerPage] = React.useState(5);

  const [rows, setRows] = React.useState<Data[]>([]);
  const [editingCell, setEditingCell] = React.useState<{ id: number; field: keyof Data } | null>(null);

  // Add a new row
  const addRow = () => {
    const newRow = createData(rows.length + 1, '', '', '', '', '', '', '');
    setRows([...rows, newRow]);
    handlePostPatient();
  };

  // Delete selected rows and update pagination
  const deleteRow = () => {
    const newRows = rows.filter((row) => !selected.includes(row.id)).map((row, index) => ({ ...row, id: index + 1 }));
    const uuids = rows.filter((row) => selected.includes(row.id)).map((row) => row.uuid);
    console.log(uuids);
    uuids.forEach((uuid) => {
      handleDeletePatient(uuid);
  });
    setRows(newRows);
    setSelected([]);
    setPage((prevPage) => Math.min(prevPage, Math.ceil(newRows.length / rowsPerPage) - 1));
  };

  const [editedRow, setEditedRow] = React.useState<{ [key: string]: any }>({});

  // Enable editing for a cell
  const handleCellClick = (id: number, field: keyof Data) => {
    setEditingCell({ id, field });
    const currentRow = rows.find((row) => row.id === id);
    setEditedRow(currentRow ? { [field]: currentRow[field] } : {});
  };
  
  // Save the cell data
  const saveCell = () => {
    if (editingCell) {
      const { id, field } = editingCell;
      setRows((prevRows) =>
        prevRows.map((row) => (row.id === id ? { ...row, [field]: editedRow[field] } : row))
      );
      setEditingCell(null);
      setEditedRow({});
    }
  };

  // Handle row selection toggle
  const handleEditChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = event.target;
    setEditedRow((prev) => ({ ...prev, [name]: value }));
  };

  // Handle row selection toggle
  const handleRowClick = (id: number) => {
    setSelected((prevSelected) =>
      prevSelected.includes(id) ? prevSelected.filter((selectedId) => selectedId !== id) : [...prevSelected, id]
    );
  };

  // Handle page change
  const handleChangePage = (event: unknown, newPage: number) => {
    setPage(newPage);
  };

  // Handle rows per page change and reset to first page
  const handleChangeRowsPerPage = (event: React.ChangeEvent<HTMLInputElement>) => {
    setRowsPerPage(parseInt(event.target.value, 10));
    setPage(0);
  };

  // Determine the rows to display based on the current page and rows per page
  const paginatedRows = rows.slice(page * rowsPerPage, page * rowsPerPage + rowsPerPage);


  /* -------------- */
  // RTK QUERY CODE FROM NOW ON!!!
  /* -------------- */

  // // POST sends an empty state to flask application
  const [postPatients] = api.endpoints.postPatient.useMutation();
  // GET receives all patient data, including UUID & refetching mechanism
  const { data: patients } = api.endpoints.getPatientAll.useQuery();
  // DELETE deletes a patient from DB
  const [deletePatient] = api.endpoints.deletePatient.useMutation();
  // PUT updates a patient giving the person new information
  const [editPatient] = api.endpoints.editPatient.useMutation();

  // Post a patient
  const handlePostPatient = async () => {
    try {
      await postPatients();
    } catch (error) {
      console.error('Failed to post patient:', error);
    }
  }

  // Delete a patient
  const handleDeletePatient = async (uuid: string) => {
    try {
      await deletePatient(uuid).unwrap();
    } catch (error) {
      console.error('Failed to delete patient:', error);
    }
  };

  // sorry for use effect, but GRANTED i think this use effect is fine becuase it resets rows AFTER patient is updated?
  // need to typescript it b/c any error do later if you feel like it @kevin
  React.useEffect(() => {
    if (patients) {
      console.log("Fetched patients:", patients); // Log to verify structure
      setRows(patients.map((patient, index) => ({
        ...patient,
        id: index + 1,
        name: patient[1] || 'No Name', // Default value if undefined
        BMI: patient[4] || 'No BMI',
        HR: patient[5] || 'No HR',
        BP: patient[6] || 'No BP',
        specialist: patient[2]|| 'No Specialist',
        patientRisk: patient[3] || 'TBD',
        uuid: patient[0]
      })));
    }
  }, [patients]);



  return (
    <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'left', minHeight: '100vh' }}>
      <Box sx={{ width: '100%', display: 'flex', justifyContent: 'center', alignItems: 'center', flexDirection: 'column' }}>
        <Paper sx={{ width: '80%', mb: 2 }}>
          <EnhancedTableToolbar numSelected={selected.length} addRow={addRow} deleteRow={deleteRow}/>
          <TableContainer>
            <Table sx={{ minWidth: 750 }} aria-labelledby="tableTitle" size={dense ? 'small' : 'medium'}>
              <EnhancedTableHead
                numSelected={selected.length}
                onSelectAllClick={(event) => {
                  const newSelected = event.target.checked ? rows.map((n) => n.id) : [];
                  setSelected(newSelected);
                }}
                rowCount={rows.length}
              />
              <TableBody>
                {paginatedRows.map((row) => {
                  const isItemSelected = selected.includes(row.id);
                  return (
                    <TableRow key={row.id}>
                      <TableCell padding="checkbox">
                        <Checkbox
                          color="primary"
                          checked={isItemSelected}
                          onClick={(event) => {
                            event.stopPropagation();
                            handleRowClick(row.id);
                          }}
                        />
                      </TableCell>
                      {['name', 'BMI', 'HR', 'BP', 'specialist'].map((field) => (
                        <TableCell
                        key={field}
                        onClick={() => handleCellClick(row.id, field as keyof Data)}
                        align={field === 'specialist' ? 'right' : field === 'BMI' ? 'right' : 'left'}
                      >
                        {editingCell?.id === row.id && editingCell.field === field ? (
                          <TextField
                          name={field}
                          onChange={handleEditChange}
                          value={editedRow[field] || ''}
                          onBlur={saveCell}
                          onKeyDown={(event) => {
                            if (event.key === 'Enter') saveCell();
                          }}
                          variant="standard"
                          autoFocus
                          />
                        ) : (
                            row[field as keyof Data]
                          )}
                        </TableCell>
                      ))}
                      <TableCell align="right">{row.patientRisk || 'TBD'}</TableCell>
                    </TableRow>
                  );
                })}
              </TableBody>
            </Table>
          </TableContainer>
          <TablePagination
            rowsPerPageOptions={[5, 10, 25, 100]}
            component="div"
            count={rows.length}
            rowsPerPage={rowsPerPage}
            page={page}
            onPageChange={handleChangePage}
            onRowsPerPageChange={handleChangeRowsPerPage}
          />
        </Paper>

        <Box sx={{ width: '80%', display: 'flex', justifyContent: 'space-between', alignItems: 'left', mt: 2 }}>
          <FormControlLabel
            control={<Switch checked={dense} onChange={(event) => setDense(event.target.checked)} />}
            label="Dense padding"
            sx={{ marginLeft: 0 }}
          />
        </Box>
      </Box>
    </div>
  );
}