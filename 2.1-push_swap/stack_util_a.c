/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   stack_util_a.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: meldemir <meldemir@student.42berlin.d      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/12 15:02:46 by meldemir          #+#    #+#             */
/*   Updated: 2026/01/12 15:02:48 by meldemir         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

int ft_is_sorted(t_list *stack)
{
    t_list *current;

    current = stack;
    while (current && current->next)
    {
        if (*(int *)current->content > *(int *)current->next->content)
            return (0);
        current = current->next;
    }
    return (1);
}

int ft_find_min(t_list *stack)
{
    t_list *temp;
    int index;
    int min;
    int pos;

    if (!stack)
        return (-1);
    temp = stack;
    index = 0;
    pos = 0;
    min = *(int *)temp->content;
    while (temp)
    {
        if (*(int *)temp->content < min)
        {
            min = *(int *)temp->content;
            pos = index;
        }
        temp = temp->next;
        index++;
    }
    return (pos);
}

int ft_find_max(t_list *stack)
{
    t_list *temp;
    int index;
    int max;
    int pos;

    if (!stack)
        return (-1);
    temp = stack;
    index = 0;
    max = *(int *)temp->content;
    while (temp)
    {
        if (*(int *)temp->content > max)
        {
            max = *(int *)temp->content;
            pos = index;
        }
        temp = temp->next;
        index++;
    }
    return (pos);
}
