from src.core import ui, duration, resource


def main():
    helptext = """Utilisez un slash '/' pour montrer un cours en Q1/Q2.
Répondez avec un underscore '_' pour signifier qu'il n'ya pas cours
Répondez avec un point '.' pour indiquer que la journée est finie. 
"""
    sched = dict()

    days = ['lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi']
    subjects = resource.get('subjects').get('subjects', [])
    if len(subjects) < 1:
        subjlist = list()
        print("Entrez vos matières\nRépondez avec un point '.' pour indiquer qu'il n'y a pas d'autres matières à "
              "ajouter.")
        subject = None
        while subject != '.':
            subject = ui.ask("Entrez un nom de matière:")
            if subject != '.':
                subjlist.append(subject)
        resource.write('subjects', {'subjects': subjlist})

        subjects = subjlist

    baseduration = ui.ask("Durée de base des cours ?", validate=duration.fromstr)
    halfhours = ui.ask(f"Y-a-t'il des cours qui ne durent pas {duration.tostr(baseduration)} ?", allow=bool,
                       default=False)
    starthour = ui.ask("À quelle heure commences-tu ?", validate=duration.fromstr)

    print(helptext)

    for day in days:
        # TODO handle Q1/Q2
        daysched = dict()
        subject = None
        current_hour = starthour
        print(f"{day.upper()}")
        print(f"{'-' * len(day)}")
        while subject != '.':
            disp_currenthour = '{h:0>2}:{m:0>2}'.format(**current_hour)

            subject = ui.ask(f"{disp_currenthour}: ", newline=False, allow=subjects + ['.','_'])
            if subject == '.':
                break

            if halfhours:
                subjduration = ui.ask("Durée du cours ?", validate=duration.fromstr,
                                      default=duration.tostr(baseduration))
            else:
                subjduration = baseduration

            daysched[disp_currenthour] = subject

            current_hour = duration.add(current_hour, subjduration)

        sched[day] = daysched

    resource.write('schedule', {'schedule': sched})


if __name__ == '__main__':
    main()
