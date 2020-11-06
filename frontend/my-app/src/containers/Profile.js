import React from 'react'
import { makeStyles } from '@material-ui/core/styles'
import Card from '@material-ui/core/Card'
import CardActions from '@material-ui/core/CardActions'
import CardContent from '@material-ui/core/CardContent'
import Button from '@material-ui/core/Button'
import Typography from '@material-ui/core/Typography'

const useStyles = makeStyles({
  root: {
    minWidth: 275,
  },
  bullet: {
    display: 'inline-block',
    margin: '0 2px',
    transform: 'scale(0.8)',
  },
  title: {
    fontSize: 14,
  },
  pos: {
    marginBottom: 12,
  },
});

const Profile=(props) => {
  const classes = useStyles()

  return (
    <Card className={classes.root}>
      <CardContent>
        <Typography className={classes.title} color="textSecondary" gutterBottom>
            Name : {props.data.first_name} {props.data.last_name}
        </Typography>
        <Typography variant="body2" component="p">
            Member ID : {props.data.id}
        </Typography>
        <Typography variant="body2" component="p">
            Email : {props.data.email}
        </Typography>
        <Typography variant="body2" component="p">
            Address : {props.data.address_line1} {props.data.address_line2}
        </Typography>
        <Typography variant="body2" component="p">
            Contact No: {props.data.contact_no1} | {props.contact_no2}
        </Typography>
        <Typography variant="body2" component="p">
            Date of Birth : {props.data.date_of_birth}
        </Typography>
        <Typography variant="body2" component="p">
            Health Problems: {props.data.health_problems}
        </Typography>
        <Typography variant="body2" component="p">
            Allergies : {props.data.allergies}
        </Typography>
        <Typography variant="body2" component="p">
            Meal Preference : {props.data.meal_preference}
        </Typography>
        <Typography variant="body2" component="p">
            Height (cm) : {props.data.height}
        </Typography>
        <Typography variant="body2" component="p">
            Gender : {props.data.gender}
        </Typography>
      </CardContent>
      <CardActions>
        <Button size="small">Edit Details</Button>
      </CardActions>
    </Card>
  )
}

export default Profile